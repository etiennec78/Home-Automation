# Automatic Gate ⛩️
## Description 📝
Modular and secure gate automation that opens your gate upon leaving or arriving
* Supports up to 10 users driving simultaneously
* Security features including an auto-close timer, alert notifications, timeout detection, aborting on vehicle left, aborting if driven near home without entering, keeping gate open while someone else approaches or leaves home
* Various options such as iBeacon automatic closing, travel time update interval, and custom gate settings

## Flowchart 🔀
[<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Automatic%20Gate/Automatic%20Gate%20Flowchart.png?raw=true" width="100%">](https://miro.com/app/board/uXjVMpH4Tno=/)

## How to Install 🚀

### Import the blueprint 🗺️
[![Import Automatic Gate blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FAutomatic%20Gate%2Fblueprint.yaml)

### Required [sensors](https://github.com/etiennec78/Home-Automation/blob/master/Automatic%20Gate/sensors.yaml) 📡
|        Sensor         |      Type      |      Provider      | Multiple |                                                      Description                                                      |
| :-------------------: | :------------: | :----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------- |
|    Driving sensor     | binary_sensor  | [Companion](https://companion.home-assistant.io/docs/core/sensors#android-auto)/[Template](https://www.home-assistant.io/integrations/template/) |   Yes    | Either Android Auto, bluetooth connexion, or both grouped                                                             |
| GPS location tracker  |     person     |     [Companion](https://companion.home-assistant.io/docs/core/location)      |   Yes    | Try to avoid using wifi/ble location trackers as latency could be an issue. Use high precision when driving near home |
|    Planned opening    | input_datetime |       [Helper](https://www.home-assistant.io/integrations/input_datetime/)       |    No    | A helper you have to create which will store the planned automatic opening of the gate                                |
|    Itinerary state    |   input_text   |       [Helper](https://www.home-assistant.io/integrations/input_text/)       |   Yes    | A helper you have to create which will store the state of each user itinerary                                         |
|      Travel time      |     sensor     |        [Waze](https://www.home-assistant.io/integrations/waze_travel_time/)        |   Yes    | For now only Waze integration accepted, calculates the travel time between you and your home. Disable auto polling    |
|     User distance     |     sensor     |     [Proximity](https://www.home-assistant.io/integrations/proximity/#distance)      |   Yes    | Distance of the user from home                                                                                        |
|    Notify service     |     service    |     [Companion](https://companion.home-assistant.io/docs/notifications/notifications-basic)      |   Yes    | Each phone per user to notify of the itinerary state. Comes by default when installing the companion app              |
|         Gate          |  switch/cover  |        Any         |    No    | Any gate or garage door which is either a switch or a cover. Could be my [esphome firmware](https://github.com/etiennec78/Home-Automation/blob/master/Automatic%20Gate/Extra/Esphome%20gate%20firmware/gate.yaml) or any other integration    |

### Optional [sensors](https://github.com/etiennec78/Home-Automation/blob/master/Automatic%20Gate/sensors.yaml) ➕
|        Sensor         |      Type      |      Provider      | Multiple |                                                      Description                                                      |
| :-------------------: | :------------: | :----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------- |
|    BLE transmitter    |      none      |     [Companion](https://companion.home-assistant.io/docs/core/sensors/#bluetooth-sensors)      |   Yes    | Companion app ble transmitter to automatically close gate upon leaving                                                  |
|  BLE scanner switch   |     switch     |        Any         |    No    | A switch which would automatically turn on/off your BLE scanner. Not useful if your BLE scanner is running 24/7       |
|     BLE entities      |signal_strength |        Any         |   Yes    | Each BLE entity to monitor when the driver BLE state goes to unavailable. Could be my [esphome firmware](https://github.com/etiennec78/Home-Automation/blob/master/Automatic%20Gate/Extra/Esphome%20gate%20firmware/gate.yaml) or else.
|  Notify all devices   |     group      |       [Group](https://companion.home-assistant.io/docs/notifications/notifications-basic/#sending-notifications-to-multiple-devices)        |    No    | Only necessary for esphome firmware and extra gate automations
|   Nearest distance    |     sensor     |     [Proximity](https://www.home-assistant.io/integrations/proximity/#nearest-distance)      |    No    | Only necessary for esphome firmware. Gives the distance of the nearest person from home.

### Install as an automation 🤖
Not recommended 🙅
1. Rename each 'user0', 'user1' and 'user2' to the person ids of each of your users.
2. Rename all your sensors id so they contain these names like in the automation (e.g : notify.mobile_app_user0_phone ) (Settings > Devices > Entities > select an entity > Settings > change their id)
3. Either copy the automation to your automations folder or simply copy and paste the code in a new automation with the UI

## Extra ➕

|          Element          |                                                                           Description                                                                            |
| :-----------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      [Automations](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Automations) 🤖       | Automations that notify all users if the gate has been left open or is unavailable for more than 5 minutes                                                       |
|     [Ble car device](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Ble%20car%20device) 🚗     | A really small Arduino code to let a ESP32 sit in your car so that your phone can connect to it over BLE and monitor if you are driving                          |
|   [ESPHome gate firmware](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Esphome%20gate%20firmware) 🔧 | My ESP32 gate firmware which only needs to be connected to one open&close pin. Works by guessing the actual state and locking new requests while not being ready |
|        [Frontend](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Frontend) 🎨        | A small dashboard which can track the position history of a user and display both the ETA and time remaining when an itinerary is in progress                    |
