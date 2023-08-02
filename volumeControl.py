"""Script for loading the config and run MQTT transfer protocol"""
from paho.mqtt import client as mqtt_client
import random
import json
import os



class VolControler():
    def __init__(self, config):
        self.broker = config['broker']
        self.port = int(config['port'])
        self.topic = config['topic']
        self.username = config['username']
        self.password = config['password']
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'

    def connect_mqtt(self) -> mqtt_client:
        """Method to connect MQQT broker"""
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        """Receive a message on subscribed toppic and trigger volume set"""
        def on_message(client, userdata, msg):
            output = json.loads(msg.payload.decode())
            value = int(json.loads(msg.payload.decode())['brightness']/255*100)
            self.update_volume(output, value)

        client.subscribe(self.topic)
        client.on_message = on_message

    def update_volume(output, value):
        """Run qdbus instruction for volume adjustment"""
        #set PulseAudio Master output volume in %
        os.system(f"pactl set-sink-volume @DEFAULT_SINK@ {value}%")
        #toggle KDE Volume OSD (on-screen-display)
        os.system(f'qdbus org.kde.plasmashell /org/kde/osdService volumeChanged {value}')
        #run specific action of Symfonisk knob
        if output['action'] == 'toggle':
            os.system('qdbus org.kde.kglobalaccel /component/mediacontrol invokeShortcut "playpausemedia"')

        elif output['action'] == 'brightness_step_up':
            os.system('qdbus org.kde.kglobalaccel /component/mediacontrol invokeShortcut "nextmedia"')

        elif output['action'] == 'brightness_step_down':
            os.system('qdbus org.kde.kglobalaccel /component/mediacontrol invokeShortcut "previousmedia"')



def run():
    config_file = open('/lib/volumeKnobController/config.json')
    config = json.load(config_file)

    vc = VolControler(config)
    client = vc.connect_mqtt()
    vc.subscribe(client)

    client.loop_forever()


if __name__ == '__main__':
    run()
