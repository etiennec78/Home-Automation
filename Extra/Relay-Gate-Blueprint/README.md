# Relay Gate ⛩️

## Description

A script to transform a basic relay switch into a proper cover entity for your gate/garage door.

> If you are using an [ESP32 with relay](https://amzn.to/3y2UtCr), you should use my [ESPHome firmware](https://github.com/etiennec78/Home-Automation/blob/master/ESPHome-Firmwares/Gate) instead

> ⚠️ Since this script uses a relay without additional sensors, it cannot detect state changes from external controls (e.g: remotes). For consistent operation, use the same control method to open and then close consecutively.

## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide

### Import the blueprint

[![Import Relay Gate blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FExtra%2FRelay-Gate%2Frelay-gate.yaml)

### Setup

1. Import the blueprint with the button above
2. Select `Relay Gate` in your [blueprint dashboard](https://my.home-assistant.io/create-link/?redirect=blueprints)
3. Fill in inputs
4. Press `Save` in the bottom right corner
5. Create a new [Virtual gate interface](../../sensors.md#virtual-gate-interface-%EF%B8%8F) (follow instructions)
