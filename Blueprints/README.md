# Blueprints 🛠️

| Blueprint | Description | Quick install |
| :---: | :---: | :---: |
| Automatic Gate ⛩️ | [Read More](Automatic-Gate) | [![Quickly import Automatic Gate](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FAutomatic-Gate%2Fautomatic-gate.yaml) |
| Itinerary Tracker Notification 📍 | [Read More](Itinerary-Tracker-Notification) | [![Quickly import Itinerary Tracker Notification](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FItinerary-Tracker-Notification%2Fitinerary-tracker-notification.yaml) |
| Gate Alerts 🚨 | [Read More](Gate-Alerts) | [![Quickly import Gate Alerts](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fetiennec78%2FHome-Automation%2Fblob%2Fmaster%2FBlueprints%2FGate-Alerts%2Fgate-alerts.yaml) |

## How to update 🔁

1. Go to [Settings > Automations & Scenes > Blueprints](https://my.home-assistant.io/redirect/blueprints)
2. Click on the three-dot menu to the right of the blueprint needing an update, and select "Re-import blueprint"
3. Optional: At the right of the blueprint, press `⁝` then `Run actions` and check your notifications for configuration errors

## How to install manually 👨‍🔧

1. Explore the [GitHub repository](https://github.com/etiennec78/Home-Automation)
2. Optional: Change the branch in the upper-left corner (master by default)
3. Copy the URL of the YAML file containing the blueprint you want to install
4. Go to your [Settings > Automations & Scenes > Blueprints](https://my.home-assistant.io/redirect/blueprints)
5. Select "Import blueprint" and paste the URL

## Config checker 🛠️✅

Each blueprint can be executed manually to verify the user's configuration

To do this, press `⁝` to the right of your automation, then press `Run actions` and check your dashboard notifications for any configuration errors

Refer to the table below to fix the errors


<details>
  <summary>Error codes table ⚠️</summary>

  | Error code | Error | Fix |
  | :---: | :--- | :--- |
  | #1 | Your custom translations are not valid | Check that your custom translations input contains a [valid json dictionary](https://jsonformatter.curiousconcept.com/) and that your strings are located in 'message', 'title' or 'button' keys, with a subkey for each message id |
  | #2 | You have not entered any iBeacon scanners | Either untick all iBeacon opening/closing inputs and remove all iBeacon related sensors in the 'Presence sensors' category, or add some iBeacon tracker entities |
  | #3 | You have entered an iBeacon scanner but are not using it | Either tick some iBeacon opening/closing inputs, or remove all iBeacon related sensors in the 'Presence sensors' category |
  | #4 | You have not entered any Wi-Fi trackers | Either untick the Wi-Fi opening input in the 'Presence sensors' category, or add some Wi-Fi trackers |
  | #5 | You have entered a Wi-Fi tracker but are not using it | Either tick the Wi-Fi opening input, or remove your Wi-Fi trackers in the 'Presence sensors' category |
  | #6 | One of the device trackers does not support GPS tracking | Replace Wi-Fi device trackers by GPS trackers in the 'Persons' input |
  | #7 | One of your iBeacon trackers is currently not reporting 'unknown'. If you are currently near your iBeacon, you can ignore this error. | Check that your iBeacon trackers go back to their 'unknown' state after losing the iBeacon for some seconds |
  | #8 | You do not have any way to detect your arrival | Please add a travel time sensor or use an iBeacon for opening on arrival |
  | #9 | You are using several methods to detect your arrival | Either untick 'Open on arrival when connected to: iBeacon' or remove your travel time sensors |
  | #10 | The maximum character length of your itinerary sensor is too short (255 is recommended) | Read [this part](https://github.com/etiennec78/Home-Automation/blob/dev/sensors.md#itinerary-sensors-%EF%B8%8F) of the wiki to change the maximum length |
  | #11 | You have not entered a consistent number of sensors between each input in the 'Per Person Sensors' category | Some fields must have exactly (or at most) one sensor per person. Make sure you comply with these conditions. |
  | #12 | You do not appear to have entered all your per person sensors in the same order | Each person must have all their 'per person sensors' at the same index |
  | #13 | Not all of your iBeacon trackers are from the same device | Please check that all of your iBeacon trackers entities are from your gate controller |
  | #14 | One of your Wi-Fi trackers is a GPS type instead of a Router type | Replace GPS device trackers by Wi-Fi trackers in the 'Wi-Fi devices' input |
  | #15 | You have not entered the sensor containing gate error codes | The 'error' notification type of this blueprint relies on a sensor providing error codes. Please ensure you have entered this sensor in the 'Error Message Sensor' input |
  | #16 | You need at least a speaker and a TTS service | Either remove your speakers and TTS service, or fill both of these inputs |
  | #17 | You have not entered any method for receiving notifications | Either use dashboard notifications, speakers, or mobile devices |
  | #18 | A bound for the speakers' night mode schedule is missing | Either fill both night start and night end inputs, or clear both |
  | #19 | One of your iBeacon transmitters is invalid | Please check your 'iBeacon transmitter entities' inputs for invalid sensors |
  
</details>
