# IKEA Symfonisk Knob System Controller

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

The IKEA Symfonisk Knob Controller Receiver is a project that allows you to receive signals from the IKEA Symfonisk knob controller based on the Zigbee protocol. By setting up a Zigbee-to-MQTT environment and running the `setup.sh` script, you can easily integrate the knob controller into your system.

...

## Prerequisites

Before running the receiver, you need the following:

- Zigbee receiver adapter to capture the signals from the IKEA Symfonisk knob controller.
  
  You can find a list of supported Zigbee adapters [here](https://www.zigbee2mqtt.io/guide/adapters/).
- Set up Zigbee-to-MQTT environment to translate Zigbee signals to MQTT messages.
  
  Here's Getting Started page of Zigbee2MQTT [link](https://www.zigbee2mqtt.io/guide/getting-started)

## Getting Started

1. Clone this repository to your local machine:

```git clone https://github.com/your-username/ikea-symfonisk-knob-receiver.git```

2. Navigate to the project directory:

```cd ikea-symfonisk-knob-receiver```

3. Run the setup script:

```./setup.sh```

The script will prompt you to provide some basic information to configure the receiver.


## Usage
After setting up the receiver, you can use the IKEA Symfonisk knob controller to control your system:

* **Right and Left Twist**: Adjusts the system volume.
* **Single Click**: Play/Pause.
* **Double Click**: Switches to the next song.
* **Triple Click**: Plays the previous song.

## Supported Environments
The current version of the repository works flawlessly on KDE flavor. Support for other environments might be added in the future.

## Linux Service
The setup script will add a Linux service to run the receiver on system boot, ensuring the controller is always ready to use.

## Contributions
Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. Feel free to use it for personal or commercial purposes.

## Acknowledgments
A big thanks to the developers and contributors of paho-mqtt for their invaluable MQTT Python client library.

:musical_note::musical_note::musical_note:
