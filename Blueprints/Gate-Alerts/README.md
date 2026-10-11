# Gate alerts 🚨

## Description 📝

A blueprint that notifies selected users when the gate:

* Opens 🔓
* Closes 🔐
* Encounters an error ⚠️
* Has been left open for too long 🔓
* Has been offline for too long 🌐❌
* Is back online 🌐✅

## Key Features 🌟

* Compatible with gate switches, covers, and position tracked covers 🔗
* Companion app notifications 🔔
* Button to close the gate from notifications 🔐
* Dashboard persistent notifications 📢
* Android TTS support 📳
* Media players TTS support 🔊
* Built-in translations 🌍
* Customizable extra actions ➕



## Notification event and lifetime options 🔔

The **Notification type** selector supports the original **Opening** and **Closing**
events, plus **Open (fully open)** and **Closed (fully closed)**:

* **Opening** / **Closing** preserve their existing trigger behavior.
* **Open (fully open)** requires a gate entity that explicitly reports `open`.
  A binary contact alone cannot confirm that the gate is fully open.
* **Closed (fully closed)** triggers when the gate reports `off` or `closed`.
  For a binary contact, `off` must mean fully closed.

**Notification lifetime** applies to all notification types:

* **Automatic (legacy)** retains the existing state-dependent dismissal rules
  for original event types; new fully-open/fully-closed events expire after 30 seconds.
* **Remove after 30 seconds** always clears the mobile notification after 30 seconds.
* **Keep notification until dismissed** does not automatically clear it.

This setting is independent of the existing dashboard persistent-notification option.
The default is **Automatic (legacy)** to preserve existing configurations.
Existing blueprint values `open` and `close` remain unchanged.

## Buy Me a Coffee ☕

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide 🚀

### Requirements 📝

* A smart gate connected to Home Assistant like my [ESPHome Gate Firmware](/ESPHome-Firmwares/Gate)

### Import the blueprint 🗺️

[![Import Gate Alerts blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FGate-Alerts%2Fgate-alerts.yaml)

### Setup 🛠️

1. Import the blueprint with the button above
2. Select `Gate Alerts` in your [blueprint dashboard](https://my.home-assistant.io/create-link/?redirect=blueprints)
3. Fill in the `Essential Inputs` category
4. Optional: Fill in other categories
5. Press `Save` in the bottom right corner
6. Optional: In the upper-right corner, press `⁝` then `Run actions` and check your dashboard notifications for configuration errors
7. Optional: On Android, go to your applications settings, then select `Home Assistant > Notifications > Gate alerts` and change the sound to differentiate your gate from other notifications


## Examples 📌

<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-left-open-notification.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-left-open-persistent.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-offline-notification.png?raw=true" width="35%">
<img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home-Automation/Blueprints/Gate-Alerts/gate-offline-persistent.png?raw=true" width="35%">
