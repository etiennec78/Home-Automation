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
  <summary><h3>Error codes table ⚠️</h3></summary>

  | Error code | Error | Fix |
  | :---: | :--- | :--- |
  | #1 | Your custom translations are not valid | Check that your custom translations input contains a [valid json dictionary](https://jsonformatter.curiousconcept.com/) and that your strings are located in 'message', 'title' or 'button' keys, with a subkey for each message id |
  | #2 | You have not entered any BLE scanners | Either untick all Bluetooth LE opening/closing inputs and remove all BLE related sensors in the 'Presence sensors' category, or add some BLE tracker entities |
  | #3 | You have entered these BLE scanners: '...' but are not using them | Either tick some Bluetooth LE opening/closing inputs, or remove all BLE related sensors in the 'Presence sensors' category |
  | #4 | You have not entered any Wi-Fi trackers | Either untick the Wi-Fi opening input in the 'Presence sensors' category, or add some Wi-Fi trackers |
  | #5 | You have entered these Wi-Fi trackers: '...' but are not using them | Either tick the Wi-Fi opening input, or remove your Wi-Fi trackers in the 'Presence sensors' category |
  | #6 | These trackers/persons: '...' do not support GPS tracking | Replace Wi-Fi device trackers by GPS trackers in the 'Persons' input |
  | #7 | These BLE trackers: '...' are currently not reporting an 'unknown' state | Check that these BLE trackers go back to their 'unknown' state after losing signal for some seconds |
  | #8 | You do not have any way to detect your arrival | Please add a travel time sensor or use an Bluetooth LE tracker for opening on arrival |
  | #9 | You are using several methods to detect your arrival | Either untick 'Open on arrival when connected to: Bluetooth LE' or remove your travel time sensors |
  | #10 | These itinerary sensors: '...' have a maximum length of less than 255 | Read [this part](https://github.com/etiennec78/Home-Automation/blob/dev/sensors.md#itinerary-sensors-%EF%B8%8F) of the wiki to change the maximum length of these helpers |
  | #11 | You have not entered a consistent number of sensors in the per person sensor inputs | Some fields must have exactly (or at most) one sensor per person. Make sure you comply with these conditions. |
  | #12 | These persons: '...' appear to have mixed up per person sensors | Each person must have all their 'per person sensors' at the same index |
  | #14 | These trackers: '...' are GPS-based, not router-based | Replace GPS device trackers by Wi-Fi trackers in the 'Wi-Fi devices' input |
  | #15 | You have not entered the sensor containing gate error codes | The 'error' notification type of this blueprint relies on a sensor providing error codes. Please ensure you have entered this sensor in the 'Error Message Sensor' input |
  | #16 | You need at least a speaker and a TTS service | Either remove your speakers and TTS service, or fill both of these inputs |
  | #17 | You have not entered any method for receiving notifications | Either use dashboard notifications, speakers, or mobile devices |
  | #18 | A bound for the speakers' night mode schedule is missing | Either fill both night start and night end inputs, or clear both |
  | #19 | These iBeacon transmitters: '...' are invalid | Please check that the iBeacon transmitter entities mentionned come from the android mobile app, and are transmitters, not monitors. Also, these sensors are not needed on iOS |
  | #20 | These persons cannot be tracked by GPS: '...' because they do not have GPS trackers, or they come from a different mobile app than the notification device | Either untick the 'gps' in the 'Confirm the location on startup' input, or check that your person entity has at least one gps device tracker, and that if it is provided by a mobile app, ensure that it is the same one as your notification device |
  
</details>
