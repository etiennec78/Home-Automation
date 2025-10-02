# Gate alerts 🚨

## Description 📝

A blueprint that **notifies** selected users when the gate:

* **Opens**
* **Closes**
* Encounters an **error**
* Has been left **open** for **too long**
* Has been **offline** for **too long**


## Key Features 🌟

* Compatible with gate switches, covers, and position tracked covers 🔗
* Companion app notifications 🔔
* Close gate button in notifications 🔐
* Dashboard persistent notifications 📢
* Android TTS support 📳
* Media players TTS support 🔊
* Built-in translations 🌍
* Customizable extra actions ➕


## Installation Guide 🚀

### Requirements 📝

* A smart gate connected to Home Assisstant like my [ESPHome Gate Firmware](/ESPHome-Firmwares/Gate)

### Import the blueprint 🗺️

[![Import Gate Alerts blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FGate-Alerts%2Fgate-alerts.yaml)

### Setup 🛠️

1. Import the blueprint with the button above
2. Select `Gate Alerts` in your [blueprint dashboard](https://my.home-assistant.io/create-link/?redirect=blueprints)
3. Fill in the `Essential Inputs` category
4. Optional: Fill in other categories
4. Press `Save` in the bottom right corner
5. Optional: In the upper-right corner, press `⁝` then `Run actions` and check your notifications for errors
6. Optional: On Android, go to your applications settings, then select `Home Assistant > Notifications > Gate alerts` and change the sound to differentiate your gate from other notifications

### How to update 🔁

Go to [Settings > Automations & Scenes > Blueprints](https://my.home-assistant.io/redirect/blueprints)

Click on the three-dot menu to the right of Gate Alerts, and select "Re-import blueprint"


## Examples 📌

<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-left-open-notification.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-left-open-persistent.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-offline-notification.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-offline-persistent.png?raw=true" width="35%">
