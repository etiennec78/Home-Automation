# ESPHome Philips LivingColors firmware 💡

## Description

A simple ESPHome configuration to hack a Philips LivingColors (Mini) with an ESP32


## Key Features

* **E1.31 protocol**: Control the light with software like [Artemis RGB](https://github.com/Artemis-RGB/Artemis)
* **Artemis layout files**: Easily Import your light into [Artemis RGB](https://github.com/Artemis-RGB/Artemis)
* **BLE Integration**: Built-in BLE tracker for automations


## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide

### Requirements

1. An [ESP32](https://amzn.to/4kNCDHc)
2. [ESPHome installed](https://esphome.io/guides/installing_esphome.html)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/etiennec78/Home-Automation.git
   ```

2. Configure the lamp:
   * Rename [secrets_example.yaml](secrets_example.yaml) to `secrets.yaml`
   * Open the file
   * Set your lamp settings
   * Fill in the required inputs

3. Flash the ESP32:
   * Connect the ESP32 to your computer
   * Execute:
     ```bash
     python -m esphome run livingcolors.yaml
     ```

4. Hardware Setup:
   * Unplug the lamp
   * Solder your ESP32
     * LivingColors: Remove power from the microcontroller, then solder your ESP32 by following the pictures below
     * LivingColors Micro: Solder pins +, -, R, G, B from the led controller to the ESP32 as shown in [this tutorial](https://thewerner.medium.com/a-brain-for-the-light-c5b290c2e31a)
   * Plug back the lamp

5. Home Assistant Integration:
   * Home Assistant should detect your ESPHome device
   * Enter API key when prompted

### Artemis RGB setup

[Artemis RGB](https://artemis-rgb.com/) is open-source lighting software which aims at grouping all peripherals into a single app to synchronize effects

With the E1.31 effect enabled by default, you can add the device to Artemis by following these steps:

1. Download and install [Artemis](https://artemis-rgb.com/)
2. Open the Plugins settings: Settings > Plugins
3. Search for the `DMX Devices` plugin and enable it
4. Click on the cog
5. In the lower-left corner, click on `Add device`
6. Fill in your device information
  * Display name: `Philips LivingColors`
  * IP: Your ESP32 local ip address
  * Port: `5568`
  * Universe: `1`
  * Model: `LivingColors`
  * Manufacturer: `Philips`
7. In the upper-right corner, click on `Add LED`
8. Click on `Save changes` for both windows
9. Open the Devices tab: Settings > Devices
10. Click on `Properties` under your Philips LivingColors
11. Go to the `Layout` tab
12. Select `Custom` as your `Layout provider`
13. Click on `Browse` to select your `Current layout`
14. Select the [./Artemis-Layout/LivingColors_Micro.xml](Artemis-Layout/LivingColors_Micro.xml) file from this repo


## Pictures

### LivingColors Micro

| | | |
| :---: | :---: | :---: |
| ![First lamp components view](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/livingcolors1.jpg?raw=true) | ![Second lamp components view](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/livingcolors2.jpg?raw=true) | ![Third lamp components view](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/livingcolors3.jpg?raw=true) |

### LivingColors

| | | |
| :---: | :---: | :---: |
| ![View of the Philips LivingColors lamp](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/normal_livingcolors.jpg?raw=true) | ![Main circuit board view with highlighted LED circuit](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/led_circuit.jpg?raw=true) | ![Touch input circuit board view](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Philips-LivingColors/touch_controller.jpg?raw=true) |
