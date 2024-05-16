# Automatic Gate ⛩️
## Description 📝
**Modular** and **secure** gate automation that **opens your gate** upon leaving or arriving
* Supports up to 10 users driving **simultaneously**
* Manual override : Prioritizes manual actions over the automation, letting you control your gate even while the automation is running
* Security features : Auto-close timer, alert notifications, timeout detection, aborting on vehicle left, aborting if driven near home without entering, keeping gate open while someone else approaches or leaves home
* Various options : Custom gate settings, iBeacon automatic closing, travel time update interval

## Flowchart 🔀
[<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Automatic%20Gate/Automatic%20Gate%20Flowchart.png?raw=true" width="100%">](https://miro.com/app/board/uXjVMpH4Tno=/)

## How to Install 🚀

### Import the blueprint 🗺️
[![Import Automatic Gate blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FAutomatic%20Gate%2Fblueprint.yaml)

### Required [sensors](sensors.md#required-sensors-) 📡
|        Sensor         |      Type      |      Provider      | Multiple |                                                       Description                                                       |
| :-------------------: | :------------: | :----------------: | :------: | :---------------------------------------------------------------------------------------------------------------------- |
|         [Gate](sensors.md#gate-%EF%B8%8F)          |  switch/cover  |        Any         |    No    | Any gate or garage door which is either a switch or a cover. Could be from my [esphome firmware](Extra/Esphome%20gate%20firmware) or any other integration |
| [GPS location trackers](sensors.md#gps-location-trackers-) |     person     |     Companion      |   Yes    | Try to avoid using wifi/ble location trackers as latency could be an issue. Use high precision when driving near home   |
|    [Driving sensor](sensors.md#driving-sensors-)     | binary_sensor  | Companion/Template |   Yes    | Either Android Auto, bluetooth connexion, or both grouped                                                               |
|      [Travel time](sensors.md#travel-time-sensors-%EF%B8%8F)      |     sensor     |        Waze        |   Yes    | For now only Waze integration accepted, calculates the travel time between you and your home. Disable auto polling      |
|   [Proximity sensors](sensors.md#proximity-sensors-%EF%B8%8F)   |     sensor     |     Proximity      |   Yes    | Calculates the distance of each user from home                                                                          |
|    [Notify services](sensors.md#notify-services-)    |     service    |     Companion      |   Yes    | Each phone notification service to notify of the itinerary status. Comes by default when installing the companion app   |
|    [Itinerary state](sensors.md#itinerary-sensors-%EF%B8%8F)    |   input_text   |       Helper       |   Yes    | A helper you have to create which will store the state of each user itinerary                                           |
|    [Planned opening](sensors.md#planned-opening-)    | input_datetime |       Helper       |    No    | A helper you have to create which will store the planned automatic opening of the gate                                  |


### Optional [sensors](sensors.md#optional-sensors-) ➕
|        Sensor         |      Type      |      Provider      | Multiple |                                                      Description                                                      |
| :-------------------: | :------------: | :----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------- |
|    [BLE transmitter](sensors.md#bluetooth-transmitter-)    |      none      |     Companion      |   Yes    | Companion app ble transmitter to automatically close gate upon leaving                                                |
|     [BLE entities](sensors.md#bluetooth-entities-)      |signal_strength |        Any         |   Yes    | Each BLE entity to monitor, to close the gate when it goes to unavailable. Could be from my [esphome firmware](Extra/Esphome%20gate%20firmware) or else  |
|  [BLE scanner switch](bluetooth-scanner-switch-)   |     switch     |        Any         |    No    | A switch which can turn on/off your BLE scanner. Not useful if you want your BLE scanner running 24/7                 |
|  [Notify all devices](sensors.md#notify-all-devices-group-)   |     group      |       Group        |    No    | Only necessary for [esphome firmware](Extra/Esphome%20gate%20firmware) and extra gate automations                                                        |
|   [Nearest distance](sensors.md#nearest-distance-sensor-)    |     sensor     |     Proximity      |    No    | Only necessary for [esphome firmware](Extra/Esphome%20gate%20firmware). Gives the distance of the nearest person from home                               |


## How to update 🔁
Simply restart Home Assistant, and this blueprint will be updated to the latest version

## Extra ➕
|          Element          |                                                                           Description                                                                            |
| :-----------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      [Automations](Extra/Automations) 🤖       | Automations that notify all users if the gate has been left open or is unavailable for more than 5 minutes                                                       |
|     [Ble car device](Extra/Ble%20car%20device) 🚗     | A really small Arduino code to let a ESP32 sit in your car so that your phone can connect to it over BLE and monitor if you are driving                          |
| [ESPHome gate firmware](Extra/Esphome%20gate%20firmware) 🔧  | My ESP32 gate firmware which only needs to be connected to one open&close pin. Works by guessing the actual state and locking new requests while not being ready |
|        [Frontend](Extra/Frontend) 🎨        | A small dashboard which can track the position history of a user and display both the ETA and time remaining when an itinerary is in progress                    |
