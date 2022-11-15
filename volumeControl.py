from paho.mqtt import client as mqtt_client
import random
import json
import os



config_file = open('/lib/volumeKnobController/config.json')
config = json.load(config_file)

broker = config['broker']
port = int(config['port'])
topic = config['topic']
username = config['username']
password = config['password']
client_id = f'python-mqtt-{random.randint(0, 1000)}'



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        output = json.loads(msg.payload.decode())
        value = int(json.loads(msg.payload.decode())['brightness']/255*100)
        update_volume(output, value)

    client.subscribe(topic)
    client.on_message = on_message


def update_volume(output, value):
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
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
