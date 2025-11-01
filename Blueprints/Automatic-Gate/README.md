# Automatic Gate ⛩️

## Description 📝

Modular and secure gate automation that opens and closes your gate upon leaving or arriving

Makes managing your gate while driving easier: You won't ever have to use your remote again


## Key Features 🌟

* **Multi-User Support**: Manages up to 10 drivers simultaneously 🚗
* **Broad Compatibility**: This blueprint is compatible with most vehicles and most travel time providers (Waze, Here, smart vehicles) 🔗
* **Notification Translations**: This blueprint ships with built-in and custom translations 🌍
* **Security & Reliability**:
  * Precise ETA calculations to have your gate fully open exactly when you arrive home 🎯
  * Vehicle status monitoring to cancel the itinerary and close the gate if you stop your vehicle or pass by without entering ✋
  * Collision prevention to ensure the gate doesn't close on anyone arriving or leaving at the same time 🚧
  * Built-in timeouts in case of an internet loss ⏳
  * Maximum entry and leaving time before auto-closing ⌛
  * Custom forbidden zones to cancel the itinerary when entered ⛔
  * Notification alerts at each decision of the automation 🚨
* **Customizable Settings**:
  * Open/Close the gate
    * Automatically 🧠
    * By asking for a confirmation ✅
    * By starting a cancellable timer ⏱️
  * Customizable gate operation timings 🛠️
  * Customizable travel time refresh rate 🔁
  * Read notifications aloud on Android 🗣️
  * Multiple gate support ⛩️
  * Open/Close with iBeacon 📡
  * House locks support 🔐
  * Avoid opening when parked near house 🅿️


## Buy Me a Coffee ☕

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide 🚀

### Requirements 📝

* A smart gate connected to Home Assistant like my [ESPHome Gate Firmware](/ESPHome-Firmwares/Gate)
* A smartphone with the companion app installed
* A vehicle compatible with Bluetooth, Android Auto, CarPlay, or an [ESP plugged into your vehicle](/Extra/ESP-Bluetooth-Dummie/esp-bluetooth-dummie.ino)
* One of these solutions to detect when you arrive:
  * A travel time service provider ([Waze](https://www.home-assistant.io/integrations/waze_travel_time/), [Here](https://www.home-assistant.io/integrations/here_travel_time/) with its ⚠️ [auto-polling disabled](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval) ⚠️ (steps 1, 2)
  * A smart vehicle providing its ETA
  * An iBeacon scanner (less recommended)
* The [Gate Alerts blueprint](../Gate-Alerts) to receive notifications when opening

### Import the blueprint 🗺️

[![Import Automatic Gate blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FAutomatic-Gate%2Fautomatic-gate.yaml)

### Setup 🛠️

1. Import the blueprint with the button above
2. Select `Automatic Gate` in your [blueprint dashboard](https://my.home-assistant.io/create-link/?redirect=blueprints)
3. Fill in `Essential Inputs` and `Per Person Sensors` categories
4. Optional: Fill in other categories
5. Press `Save` in the bottom right corner
6. Optional: In the upper-right corner, press `⁝` then `Run actions` and check your dashboard notifications for configuration errors
7. Setup the [Gate Alerts blueprint](../Gate-Alerts) to receive notifications when opening
