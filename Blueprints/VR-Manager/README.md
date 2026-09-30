# VR Manager 🥽

## Description

A blueprint that sets up the devices in your room to play VR


## Features

* Built-in configuration checker

When a VR session starts:

* Confirm the user presence in the room/house
* Ask the user for a confirmation via a notification
* Turn on computer
* Turn on lights for inside-out tracking
* Launch a PCVR streaming app
* Send a notification
* Run custom actions
* Continuously adapt the lights while playing, thanks to:
  * illuminance sensor
  * sun elevation
  * windows orientation

When the session ends:

* Restore the lights
* Turn off computer
* Run custom actions


## Support me

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C5XVRMM)


## Installation Guide

### Import the blueprint

[![Import VR Manager blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FVR-Manager%2Fvr-manager.yaml)

### Setup

1. Import the blueprint with the button above
2. Select `VR Manager` in your [blueprint dashboard](https://my.home-assistant.io/create-link/?redirect=blueprints)
3. Fill in the inputs
4. Press `Save` in the bottom right corner
5. Optional: In the upper-right corner, press `⁝` then `Run actions` and check your dashboard notifications for configuration errors
6. Read [this](../) page about my blueprints
