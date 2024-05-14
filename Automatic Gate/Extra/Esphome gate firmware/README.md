# Esphome Gate Firmware 🔧
## Description
An [ESP32](https://amzn.to/3y2UtCr) firmware I use to **smartify** my FAAC E024S **gate**

Supports the following features :
* Only accepting open requests when someone is nearer than **1km from home**
* Only accepting requests when **ready**, to avoid double presses which would make it report the wrong state
* Only using **one pin**, to only use one relay and work by **guessing** the actual state of the gate
* Opening and closing **even while moving**, by sending a double pulse, and inverting time taken to move to the current position
* **Error reporting** in HA, to see why the gate decided not to move
* **BLE scanner**, with automatically turns entity status to unavailable after no signal for 25s
* **BLE switch**, which allows you to **turn off** the continuous BLE scanning

## Flowchart 🔀

[<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Automatic%20Gate/Automatic%20Gate%20Flowchart.png?raw=true" width="100%">](https://miro.com/app/board/uXjVMpH4Tno=/)

## How to install 🚀
1. Get yourself an [ESP32 with relay](https://amzn.to/3y2UtCr), and  [Install ESPHome](https://esphome.io/guides/installing_esphome.html)
2. Read your gate documentation and identify the pin responsible for gate opening
3. Read your ESP32 documentation and identify the pin used for the relay ([this model](https://amzn.to/3y2UtCr) has it on GPIO16 or GPIO17)
4. Clone this repository, change the GPIO to your need, adapt any "!secret" line with your own information, and don't forget to change the 42s gate moving time !
5. Plug your ESP32 into your computer and run the following command to flash it : ```python -m esphome run gate.yaml```
6. Run a cable between your gate opening pin and your ESP32 relay pin, and either power your ESP32 with a gate pin, or an external supply
7. Home Assistant should detect your ESPHome device automatically on your LAN
