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


## Closure messages

For a binary contact, `off` must mean fully closed. The closing event then
reports "Gate closed", rather than "Gate closing". A cover reporting `closed`
also selects the closed message. Switches and input booleans keep their command
semantics: turning off alone does not confirm physical closure.

The automatic lifecycle is unchanged: a cover completing `closing -> closed`
clears the movement notification. The optional retained-confirmation behavior is described below.

## Retained closure confirmation

Enable **Keep closed confirmation** to always confirm physical closure, including
`closing -> closed` covers, and keep that confirmation beyond 30 seconds. Select
the existing **Closing** event; no additional event type is needed. This option
defaults to off and does not turn a switch/input boolean command into position
feedback. A binary contact must report `off` only when fully closed.

The confirmation remains dismissible and is removed when the gate leaves its
closed state, including when the sensor becomes unknown/unavailable. It has a
separate tag scoped to the automation, so a movement notification cannot clear
it. Physical closure clears the previous movement alert for the same recipients.
The confirmation uses the existing closed translations. With zero delay, a
cover's completed movement does not repeat TTS or extra actions already invoked
for its closing transition.

With the option off, direct closure confirmations retain the 30-second lifecycle;
the usual `closing -> closed` movement completion clears the closing alert.
Other alert types retain their existing lifecycle.

### Validation and limits

Offline tests render templates extracted from this blueprint (PyYAML and Jinja2):
`python -m unittest discover -s tests -p "test_gate_alerts*.py" -v`.
These checks do not execute the complete Home Assistant automation engine or
simulate asynchronous notification delivery.

The combined candidate was loaded on Home Assistant 2026.10.4. The retained
confirmation was tested with a real gate contact and Android: delivery, presence
after more than 40 seconds, manual dismissal, another closure notification and
automatic removal upon reopening all passed. Eight classification cases were
also rendered in Home Assistant's template engine.

Cover transitions are covered by offline template tests, not real cover hardware.
iOS delivery and 30-second expiry have not been verified in real conditions.
Waits do not survive automation reloads/restarts: an existing short-lived iOS or
dashboard confirmation can outlive its timer until subsequent cleanup. Retained
confirmations are cleared on subsequent non-closed state transitions; startup
cleanup of a non-closed gate depends on enabling configuration checks on load.
The generation check prevents an older closure from clearing a newer one in the
tested templates, but checking state and calling a notification service are not
atomic; rapid asynchronous cycles are not proven by these tests. The distinct
confirmation tag does not guarantee a silent notification on every platform.

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
