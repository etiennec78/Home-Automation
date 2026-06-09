# ESPHome Velux Roller Shutter 🪟

## Description

An ESPHome firmware for automating roller shutters using an [ESP32 C3](https://amzn.to/4ncZw8H) microcontroller

Compatible with [KLI 310](https://amzn.to/4eJeVcS) and 860963 Velux remotes


## Key Features

* **Physical & Remote Input**: Handles both controls with proper state feedback
* **Bidirectional Control**: Supports opening/closing even while the shutter is in motion
* **Position Control**: Precise shutter positioning through cover entity
* **Real-Time Position**: Continuously reports position as the shutter moves
* **BLE Integration**: Built-in BLE tracker for automations


## Buy Me a Coffee

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide

### Requirements

* An [ESP32 C3](https://amzn.to/4ncZw8H)
* [ESPHome](https://esphome.io/guides/installing_esphome.html) installed
* A [Velux KLI 310](https://amzn.to/4eJeVcS) remote

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/etiennec78/Home-Automation.git
   ```

2. Configure the shutter:
   * Rename [secrets_example.yaml](secrets_example.yaml) to `secrets.yaml`
   * Open the file
   * Set your shutter settings
   * Fill in the required inputs

3. Flash the ESP32:
   * Connect the ESP32 to your computer
   * Execute:
     ```bash
     python -m esphome run velux-shutter.yaml
     ```

4. Hardware Setup:
   * Remove batteries from the remote
   * Solder the [remote pins](https://github.com/yannikmotzet/velux-integra-control#wiring) to the ESP32
   * Connect your ESP32 to a power supply

5. Home Assistant Integration:
   * Home Assistant should detect your ESPHome device
   * Enter API key when prompted


## Pictures

| Internals | Cover | Demo |
| :---: | :---: | :---: |
| ![Remote internals and esp32](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Velux-Shutter/internals.jpg?raw=true) | ![Remote cover](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Velux-Shutter/cover.jpg?raw=true) | ![Demo view](https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/ESPHome-Firmwares/Velux-Shutter/demo.jpg?raw=true) |
