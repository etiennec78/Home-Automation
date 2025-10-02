# Esphome Gate Firmware ⚙️

## Description

An [ESP32](https://amzn.to/3y2UtCr) firmware I use to **smartify** my FAAC [E024S](https://faac.fr/Docs/Documentations%20techniques/13%20PLATINE_ELECTRONIQUE/E024S/RevE/E024S_732642RevE_FR.pdf) **gate**

Supports the following features :

* Only accepting open requests when someone is nearer than **1km from home** 📏
* Only accepting requests when **ready**, to avoid double presses which would make it report the wrong state ✅
* Only using **one pin**, to only use one relay and work by **guessing** the actual state of the gate 💡
* Opening and closing **even while moving**, by sending a double pulse, and inverting time taken to move to the current position 🔄
* **Error reporting** in HA, to see why the gate decided not to move ⛔
* **BLE scanner**, with automatically turns entity status to unavailable after no signal for 25s 📡
* **BLE switch**, which allows you to **turn off** the continuous BLE scanning ⏯️

*Note : Since this gate firmware relies on a single opening pin without any extra sensors, please keep in mind that it won't be able to register any state change from another source than itself. If you open your gate with your remote, please also close it with your remote, as closing with your esp32 would invert the virtual state of the gate*

## Flowchart 🔀

[<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/flowchart.png?raw=true" width="100%">](https://miro.com/app/board/uXjVMpH4Tno=/)

## How to install 🚀

### Prerequisites 📝

1. An [ESP32 with relay](https://amzn.to/3y2UtCr)
2. [ESPHome installed](https://esphome.io/guides/installing_esphome.html)
3. Your gate documentation to identify the gate opening/closing pin
4. Your ESP32 documentation to identify the pin used for the relay ([this model](https://amzn.to/3y2UtCr) uses GPIO16 and GPIO17)
5. Home Assistant sensors : [Persons](/sensors.md#gps-location-trackers-), [Proximity sensors](/sensors.md#proximity-sensors-), [Notify group](/sensors.md#notify-all-devices-group-), optional : [phone iBeacons UUIDs](/sensors.md#bluetooth-transmitter-)

### Steps 📜

1. Clone this repo
    * Run : `git clone https://github.com/etiennec78/Home-Automation.git`
2. Edit [the file](gate.yaml) to fill your needs
    * Change the GPIO pin
    * Replace any "!secret" line with your own information
    * Adapt the gate moving time (default 42s)
3. Flash your ESP32
    * Plug it into your computer
    * Run : `python -m esphome run gate.yaml`
4. Harware connections
    * Run a cable between your gate opening/closing pin and your ESP32 relay pin
    * Either power your ESP32 with a gate pin, or an external supply
5. Connect your ESP32 to Home Assistant
    * Home Assistant should detect your ESPHome device automatically on your LAN
    * Connect it and enter your api_key
    * Finally, go to *[Settings > Devices & services > ESPHome](https://my.home-assistant.io/redirect/integration/?domain=esphome) > three-dot menu to the right of your gate > Configure > Allow the device to make Home Assistant service calls ✔*

# Pictures 📷

|       |       |       |
| :---: | :---: | :---: |
| <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/whole.jpg?raw=true" width="100%" alt="Whole view" > | <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/case.jpg?raw=true" width="100%" alt="Case view"> | <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/esp.jpg?raw=true" width="100%" alt="Close view"> |
