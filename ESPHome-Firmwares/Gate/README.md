# ESPHome Gate Firmware ⛩️

## Description

An ESPHome firmware for automating gates using an [ESP32](https://amzn.to/3y2UtCr) microcontroller. It integrates seamlessly with Home Assistant to provide smart gate control functionality


## Key Features

* **Proximity-based Access**: Only accepts open requests when users are within 1km of home
* **Queue System**: Prevents the controller from sending two pulses too quickly
* **Single Pin Operation**: Uses state inference to control the gate with just one relay
* **Bidirectional Control**: Supports opening/closing even while the gate is in motion
* **Position Control**: Precise gate positioning through cover entity
* **Real-Time Position**: Continuously reports position as the gate moves
* **BLE Integration**: Built-in BLE tracker for automations

> ⚠️ Since this firmware uses a single control pin without additional sensors, it cannot detect state changes from external controls (e.g., remotes). For consistent operation, use the same control method to open and then close consecutively.

> ⚠️ Be aware that this firmware could contain bugs, so please read the code carefully and try it on a bare ESP32 first


## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide

### Requirements

* [ESP32 with relay module](https://amzn.to/3y2UtCr)
* [ESPHome](https://esphome.io/guides/installing_esphome.html) installed
* Gate documentation (for control pin identification)
* ESP32 documentation to identify relay pins ([this model](https://amzn.to/3y2UtCr) uses GPIO16 and GPIO17)
* Home Assistant sensors:
   * [Persons](/sensors.md#gps-location-trackers--persons-)
   * [Nearest distance sensor](/sensors.md#nearest-distance-sensor-)

### Setup 

1. Clone the repository:
   ```bash
   git clone https://github.com/etiennec78/Home-Automation.git
   ```

2. Configure the gate:
   * Rename [secrets_example.yaml](secrets_example.yaml) to `secrets.yaml`
   * Open the file
   * Set your gate settings
   * Fill in the required inputs
   * Set your optional inputs as needed, and uncomment "Optional" lines in [gate.yaml](gate.yaml) accordingly

3. Flash the ESP32:
   * Connect the ESP32 to your computer
   * Execute:
     ```bash
     python -m esphome run gate.yaml
     ```

4. Hardware Setup:
   * Connect the gate control pin to the ESP32 relay
   * Connect a power supply

5. Home Assistant Integration:
   * Home Assistant should detect your ESPHome device
   * Enter API key when prompted
   * Enable device service calls: [Settings > Devices & services > ESPHome](https://my.home-assistant.io/redirect/integration/?domain=esphome) > three-dot menu to the right of your gate > Configure > Allow the device to make Home Assistant service calls ✔
   * Import and configure [Gate Alerts](/Blueprints/Gate-Alerts)

### Gate Operation Logic

The firmware supports two operation modes: Normal and Inverted

The tables below show the number of pulses required to stop/open/close, depending on the current state

#### Inverted Mode

The gate closes on pulse while opening

| State | Stop | Open | Close |
| :--- | :---: | :---: | :---: |
| Open | 0 | 0 | 1 |
| Closed | 0 | 1 | 0 |
| Opening | 1 | 0 | 2 |
| Closing | **2** | **1** | 0 |
| Paused (o) | 0 | **2** | 1 |
| Paused (c) | **-** | **-** | **-** |

#### Normal Mode

The gate stops on pulse while opening

| State | Stop | Open | Close |
| :--- | :---: | :---: | :---: |
| Open | 0 | 0 | 1 |
| Closed | 0 | 1 | 0 |
| Opening | 1 | 0 | 2 |
| Closing | **1** | **2** | 0 |
| Paused (o) | 0 | **3** | 1 |
| Paused (c) | **0** | **1** | **3** |


## Error states

| State | Meaning |
| :---: | :---: |
| `nobody_near_home` | No one was close enough to the gate to allow it to open |


## Pictures

| Complete Setup | Enclosure | ESP32 Module |
| :---: | :---: | :---: |
| ![Complete Setup](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/whole.jpg?raw=true) | ![Enclosure](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/case.jpg?raw=true) | ![ESP32 Module](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Gate/esp.jpg?raw=true) |
