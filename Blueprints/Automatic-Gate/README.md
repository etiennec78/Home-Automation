# Automatic Gate ⛩️

## Description 📝

**Modular** and **secure** gate automation that **opens your gate** upon leaving or arriving
Makes managing your gate while driving easier : don't ever touch your screen or remote again
Have your gate greet you when you arrive home and be ready for you
Customize the options to tailor the system to your exact needs

## Key Features 🌟

* **Automatic Opening**: Your gate will open automatically when you drive home. No need to press any buttons ! 🏠
* **Smart Navigation**: Directly open the gate when leaving home, or launch an itinerary when starting from outside 🚀
* **Multi-User Support**: Manages up to 10 drivers simultaneously 🚗
* **Collision Prevention**: Ensures the gate doesn't close on anyone arriving or leaving at the same time 🚧
* **Security & Reliability**:
  * Precise Waze and ETA calculations to have your gate fully open exactly when you arrive home 🎯
  * Real-time position tracking to adjust timing for traffic or if you pass by without entering 📍
  * Car status monitoring to cancel everything if you leave your car ✋
  * Built-in timeouts in case of an internet loss ⏳
  * Maximum entry and leaving time before auto-closing ⌛
  * Notification alerts at each decision of the automation 🚨
  * Manual actions prioritized over the automation, letting you control your gate even while the automation is running ✍️
* **Customizable Settings**:
  * Auto-close with iBeacon 📡
  * Adjustable notifications 💬
  * Customizable security options 🔒
  * Customizable gate operation timings 🛠️
  * Customizable travel time refresh rate 🔁
  * Multiple gates supported by reusing the blueprint ♻️

## Flowchart 🔀

[<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/flowchart.png?raw=true" width="100%">](https://miro.com/app/board/uXjVMpH4Tno=/)

## How to Install 🚀

### Import the blueprint 🗺️

[![Import Automatic Gate blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FAutomatic-Gate%2Fautomatic-gate.yaml)

### Required [sensors](/sensors.md#required-sensors-) 📡

|        Sensor         |      Type      |      Provider      | Multiple |                                                       Description                                                       |
| :-------------------: | :------------: | :----------------: | :------: | :---------------------------------------------------------------------------------------------------------------------- |
|         [Gate](/sensors.md#gate-%EF%B8%8F)          |  switch/cover  |        Any         |    No    | Any gate or garage door which is either a switch or a cover. Could be from my [esphome firmware](/Esphome-Firmwares/ESPHome-Firmwares/Gate) or any other integration |
| [GPS location trackers](/sensors.md#gps-location-trackers-) |     person     |     Companion      |   Yes    | ⚠️ Use [high precision while driving near home](/sensors.md#gps-location-trackers-) or you could time out. Try to avoid using BLE/Wifi location trackers      |
|    [Driving sensor](/sensors.md#driving-sensors-)     | binary_sensor  | Companion/Template |   Yes    | Either Android Auto, bluetooth connexion, or both grouped                                                               |
|      [Travel time](/sensors.md#travel-time-sensors-%EF%B8%8F)      |     sensor     |        Waze        |   Yes    | For now only Waze integration accepted, calculates the travel time between you and your destination                 |
|   [Proximity sensors](/sensors.md#proximity-sensors-)   |     sensor     |     Proximity      |   Yes    | Calculates the distance of each user from the targetted zone                                                             |
|    [Notify services](/sensors.md#notify-services-)    |     service    |     Companion      |   Yes    | Each phone notification service to notify of the itinerary status. Comes by default when installing the companion app   |
|    [Itinerary state](/sensors.md#itinerary-sensors-%EF%B8%8F)    |   input_text   |       Helper       |   Yes    | A helper you have to create which will store the state of each user itinerary                                           |
|    [Planned opening](/sensors.md#planned-opening-)    | input_datetime |       Helper       |    No    | A helper you have to create which will store the planned automatic opening of the gate                                  |


### Optional [sensors](/sensors.md#optional-sensors-) ➕

|        Sensor         |      Type      |      Provider      | Multiple |                                                      Description                                                      |
| :-------------------: | :------------: | :----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------- |
|    [BLE transmitter](/sensors.md#bluetooth-transmitter-)    |      none      |     Companion      |   Yes    | Companion app ble transmitter to automatically close gate upon leaving                                                |
|     [BLE entities](/sensors.md#bluetooth-entities-)      |signal_strength |        Any         |   Yes    | Each BLE entity to monitor, to close the gate when it goes to unavailable. Could be from my [esphome firmware](/Esphome-Firmwares/ESPHome-Firmwares/Gate) or else  |
|  [BLE scanner switch](/sensors.md#bluetooth-scanner-switch-)   |     switch     |        Any         |    No    | A switch which can turn on/off your BLE scanner. Not useful if you want your BLE scanner running 24/7                 |
|   [Nearest distance](/sensors.md#last-notification-)   | input_datetime |       Helper       |    No    | Only necessary for [itinerary tracker notification](Extra/Automations). Stores the timestamp of the last tracking notification sent        |
|  [Notify all devices](/sensors.md#notify-all-devices-group-)   |     group      |       Group        |    No    | Only necessary for [esphome firmware](/Esphome-Firmwares/ESPHome-Firmwares/Gate). Allows it to notify all devices when opening on in case of an error       |


## How to update 🔁

Go to [Settings > Automations & Scenes > Blueprints](https://my.home-assistant.io/redirect/blueprints)

Click on the three-dot menu to the right of Automatic Gate, and select "Re-import blueprint"
