## Gate ⛩️

The entity representing your gate or garage door

This can come from my [ESPHome firmware](ESPHome-Firmwares/Gate) or any other integration

#### Supported Gate Types ⚙️

There are two main types of gate entities you can use:

1. State-based gates: entities that stay ON while open and OFF when closed
   These are fully compatible with the blueprints from this repo

2. Pulse-triggered gates: entities that briefly turn ON then OFF to send a pulse to the gate motor
   These need workarounds to make them work with the blueprints from this repo
    <details>
      <summary>Read more</summary>
      These gates cannot reliably handle the closing sequence automatically, because they do not know their own position

      Sending another pulse while still opening may simply stop the gate instead of closing it

      To use such gates:

      * Option 1: Disable the closing behavior in the blueprint settings
      * Option 2: Use the [ESPHome Gate Firmware](ESPHome-Firmwares/Gate), which supports pulse-triggered gates correctly
      * Option 3: If you have three separate pulse triggers (for open / close / stop), you can combine them into a single gate entity using a [state-based template cover](https://www.home-assistant.io/integrations/template/#state-based-cover---garage-door)
    </details>
  

## GPS location trackers / Persons 🌎

Each GPS device tracker needed to track your position

#### Summary 📝

Less frequent location updates can impact ETA accuracy

| Service | Location frequency |
| :--- | :---: |
| Android 📱 | 🟩 |
| iPhone 📱 | 🟨 |
| Smart vehicle 🌐 | ❓ |

❓: Depending on vehicle model

<details>
  <summary><h4>Option 1: Android or iPhone 📱</h4></summary>

  #### Setup 🛠️

  1. Install through the [companion app](https://companion.home-assistant.io/docs/core/location/) settings: Settings > Companion app > Manage sensors > Background location ✔
  2. Apply the settings from below
  3. Assign the trackers to a person: [Settings > People](https://my.home-assistant.io/redirect/people/) > *Select a user* > Track devices > *Your new device tracker*
  4. Repeat steps 1-3 for each user

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | High accuracy mode | ✅ |
  | High accuracy mode only when connected to BT devices | *Select vehicles bluetooth devices* |
  | High accuracy mode only when entering zone | `zone.home` *(your gate zone)* |
  | High accuracy mode trigger range for zone | *The range in which you want your phone to send frequent location updates when arriving (suggested: 1000m)* |
  | High accuracy interval | `5s` |
  | High accuracy mode only when connected to BT devices | ✅ |
  | Minimal precision | *If your position seems off, please decrease this value* |
  | Location sent | `Exact` |

  #### Extra: Requesting manual GPS updates 🧭

  Some blueprint inputs can be enabled to request manual GPS updates from the mobile app.

  To make this work, you need to enable the "Single accurate location" sensor : Settings > Companion app > Manage sensors > Single accurate location ✔

  > [!TIP]
  > If high precision mode does not trigger, please increase its range or check its conditions

</details>

<details>
  <summary><h4>Option 2: Smart vehicle 🌐</h4></summary>

  Some Home Assistant vehicle integrations or add-ons create a device_tracker that can be used to track your vehicle GPS location

</details>


## Driving sensors 🚗

Each driving sensor that detects when you start and stop driving

Use Android Auto, Apple CarPlay, Bluetooth, or a combination of these

If your vehicle does not support any of these, you can buy a [Bluetooth-to-jack adapter](https://amzn.to/3G0vOCT), a [Bluetooth-to-radio adapter](https://amzn.to/4jVEoRp), or use an [ESP32 emulating a Bluetooth keyboard](./Extra/ESP-Bluetooth-Dummie)

#### Summary 📝

| Service | Wireless | Reliability | Compatibility |
| :--- | :---: | :---: | :---: |
| Android Bluetooth 🍏🛜 | ✅ | 🟩 | Android 5+ |
| iOS Bluetooth 🍎🛜 | ✅ | 🟩 | iOS 15+ |
| Android Auto 🍏🔌 | ❓ | 🟩 | Android 9+ |
| Apple CarPlay 🍎🔌 | ❓ | 🟩 | iOS 15+ |
| Cycling (Android) 🍏🚲 | ✅ | 🟧 | Android 10+, with Google Services |
| Cycling (iOS) 🍎🚲 | ✅ | 🟧 | ❓ |
| Smart vehicle 🌐 | ✅ | ❓ | - |

<details>
  <summary><h4>Option 1: Android Bluetooth 🍏🛜</h4></summary>

  ### Setup 🛠️

  1. Install through the [companion app](https://companion.home-assistant.io/docs/core/sensors/#bluetooth-sensors) settings: Settings > Companion app > Manage sensors > Bluetooth connection ✔
  2. Install a [template helper](https://www.home-assistant.io/integrations/template/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Template > Binary sensor
  3. Apply the settings from below

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 driving` |
  | State template | `{{ '00:00:00:00:00:00 (BT-Device)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}` |
  | Device class | `Moving` |
  | Device | *Your phone* |

  Where:

  * `00:00:00:00:00:00` is your vehicle MAC address
  * `BT-Device` is the device name of your vehicle
  * `sensor.user0_bluetooth_connection` is your Bluetooth companion app sensor
  * `connected_paired_devices` needs to be left untouched

</details>

<details>
  <summary><h4>Option 2: iOS Bluetooth 🍎🛜</h4></summary>

  #### Setup 🛠️

  1. Add an [input boolean helper](https://www.home-assistant.io/integrations/input_boolean/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Toggle
  2. Name the sensor as you wish
  3. Ensure that you have paired your vehicle to your phone
  4. Import these Apple Shortcuts: [connection](https://www.icloud.com/shortcuts/f211cc4d6ac7414f852618a018bbafa4), [disconnection](https://www.icloud.com/shortcuts/6d186bbb01c54cc5b23e106f42b6d541)
  5. Tap on `Configure shortcut`
  6. Change the entity_id to the one you created in step 2
  7. Tap on `Add this shortcut`
  8. Go into the `Automation` tab
  9. Tap on `+` in the upper-right corner or the `New Automation` button
  10. Scroll down to Bluetooth
  11. Tap on `Choose` to the right of `Device`
  12. Select your vehicle bluetooth connection and press `Done`
  13. Choose `When: Is Connected`, and tick `Run Immediately`
  14. Tap on `Next` in the upper-right corner
  15. In the `My shortcuts` section, please tap on `Automatic Gateway - Car Connection`
  16. Repeat steps 8-16 but set the trigger to `When: Is Disconnected` and the blueprint to `Car Disconnection`
  17. Execute both blueprints once to select your Home Assistant server

</details>

<details>
  <summary><h4>Option 3: Android Auto 🍏🔌</h4></summary>

  #### Setup 🛠️

  * Install through the [companion app](https://companion.home-assistant.io/docs/core/sensors#android-auto) settings: Settings > Companion app > Manage sensors > Android Auto ✔

</details>

<details>
  <summary><h4>Option 4: Apple CarPlay 🍎🔌</h4></summary>

  #### Setup 🛠️

  1. Add an [input boolean helper](https://www.home-assistant.io/integrations/input_boolean/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Toggle
  2. Name the sensor as you wish
  3. Ensure that you have paired your vehicle to your phone
  4. Import these Apple Shortcuts: [connection](https://www.icloud.com/shortcuts/f211cc4d6ac7414f852618a018bbafa4), [disconnection](https://www.icloud.com/shortcuts/6d186bbb01c54cc5b23e106f42b6d541)
  5. Tap on `Configure shortcut`
  6. Change the entity_id to the one you created in step 2
  7. Tap on `Add this shortcut`
  8. Go into the `Automation` tab
  9. Tap on `+` in the upper-right corner or the `New Automation` button
  10. Scroll down to CarPlay
  11. Choose `When: Connects`, and tick `Run Immediately`
  12. Tap on `Next` in the upper-right corner
  13. In the `My shortcuts` section, please tap on `Automatic Gateway - Car Connection`
  14. Repeat steps 8-13 but set the trigger to `When: Disconnects` and the blueprint to `Car Disconnection`
  15. Execute both blueprints once to select your Home Assistant server

</details>

<details>
  <summary><h4>Option 5: Cycling (Android) 🍏🚲</h4></summary>
  
  It is recommended to use a travel time supporting cycling mode, or a BLE tracker
  
  Both opening and closing behaviors on departure should be disabled, as cycling sensors are not reliable
  
  If you are using this blueprint both for cycling and for your vehicles, please use 2 distinct automations running this blueprint, and don't forget to share all of your itinerary sensors in both

  #### Setup 🛠️

  1. Install through the [companion app](https://companion.home-assistant.io/docs/core/location/) settings: Settings > Companion app > Manage sensors > Detected Activity ✔
  2. Install a [template helper](https://www.home-assistant.io/integrations/template/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Template > Binary sensor
  3. Apply the settings from below
  4. Repeat steps 1-3 for each cyclist

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 cycling` |
  | State template | `{% set s = state_attr('sensor.user0_detected_activity', 'on_bicycle') %}{{ s | is_number and s > 80 }}` |
  | Device class | `Moving` |
  | Device | *Your phone* |

  > Replace `sensor.user0_detected_activity` with your own sensor entity id, and change `80` if the confidence is too high and the condition is never triggered

</details>

<details>
  <summary><h4>Option 6: Cycling (iOS) 🍎🚲</h4></summary>
  
  It is recommended to use a travel time supporting cycling mode, or a BLE tracker
  
  Both opening and closing behaviors on departure should be disabled, as cycling sensors are not reliable
  
  If you are using this blueprint both for cycling and for your vehicles, please use 2 distinct automations running this blueprint, and don't forget to share all of your itinerary sensors in both

  #### Setup 🛠️

  1. Install through the [companion app](https://companion.home-assistant.io/docs/core/location/) settings: Settings > Companion app > Manage sensors > Activity Sensor ✔
  2. Install a [template helper](https://www.home-assistant.io/integrations/template/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Template > Binary sensor
  3. Apply the settings from below
  4. Repeat steps 1-3 for each cyclist

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 cycling` |
  | State template | `{% set s = 'sensor.user0_detected_activity' %}{{ is_state(s, 'Cycling') and is_state_attr(s, 'confidence', 'High') }}` |
  | Device class | `Moving` |
  | Device | *Your phone* |

  > Replace `sensor.user0_detected_activity` with your own sensor entity id, and change `High` to Medium or Low if the confidence is too high and the condition is never triggered
  
</details>

<details>
  <summary><h4>Option 7: Smart vehicle 🌐</h4></summary>

  Some Home Assistant vehicle integrations or add-ons create a binary_sensor that reports when your vehicle is being driven

</details>

<details>
  <summary><h4>Combining these sensors 🔗</h4></summary>

  If some users have multiple vehicles, you can merge all sensors into one with this template.
  
  Also, for the same car, some driving sensors can be quick but less reliable (e.g.: Bluetooth vs plugged CarPlay). By merging them you can benefit form the reactivity and the reliability.

  #### Setup 🛠️

  1. Install sensors from any option above
  2. Install a [template helper](https://www.home-assistant.io/integrations/template/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Template > Binary sensor
  3. Apply the settings from below

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 driving` |
  | State template | `{{ is_state('sensor.first_sensor', 'on') or is_state('sensor.second_sensor', 'on') }}` |
  | Device class | `Moving` |
  | Device | *Your phone* |

  > Replace `sensor.first_sensor` and `sensor.second_sensor` with your own sensor entity ids

</details>


## Travel time sensors ✈️

Each travel time sensor monitoring each user's time left before arrival

#### Summary 📝

| Service | Supported | Reliability | Free | No credit card required |
| :--- | :---: | :---: | :---: | :---: |
| Here Travel Time 🚘 | ✅ | 🟩 | 🟢 | ❌ |
| Google Maps Travel Time 🚘 | ✅ | 🟩 | ✅ | ❌ |
| Waze Travel Time 🚘 | ✅ | 🟧 | ✅ | ✅ |
| Smart vehicle 🌐 | ❓ | ❓ | ❓ | ❓ |

❓: Depending on vehicle model

🟢: Free until a limit is reached

> [!WARNING]
> Please [disable sensor auto-polling (steps 1, 2)](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval), as the Automatic Gate will refresh the sensor itself

> [!WARNING]
> Please note that I am not responsible for any charges incurred by travel time services

<details>
  <summary><h4>Option 1: Here Travel Time 🚘</h4></summary>

  #### Setup 🛠️

  1. Install [HERE Travel Time](https://www.home-assistant.io/integrations/here_travel_time/) integration through the UI: [Settings > Devices & services > Add integration > HERE Travel Time](https://my.home-assistant.io/redirect/config_flow_start/?domain=here_travel_time)
  2. Apply the settings from below
  3. ⚠️ [Disable sensor auto-polling (steps 1, 2)](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval)
  4. Repeat steps 1-3 for each user

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 Travel Time` |
  | Origin | `person.user0` |
  | Destination | `zone.home` *(your gate zone)* |
  | Region | Select your region |

</details>

<details>
  <summary><h4>Option 2: Google Travel Time 🚘</h4></summary>

  #### Setup 🛠️

  1. Install [Google Maps Travel Time](https://www.home-assistant.io/integrations/google_travel_time/) integration through the UI: [Settings > Devices & services > Add integration > Google Maps Travel Time](https://my.home-assistant.io/redirect/config_flow_start/?domain=google_travel_time)
  2. Apply the settings from below
  3. ⚠️ [Disable sensor auto-polling (steps 1, 2)](https://www.home-assistant.io/integrations/google_travel_time/#defining-a-custom-polling-interval)
  4. Repeat steps 1-3 for each user

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 Travel Time` |
  | API key | *Your api key* |
  | Origin | `person.user0` |
  | Destination | `zone.home` *(your gate zone)* |

</details>

<details>
  <summary><h4>Option 3: Waze Travel Time 🚘</h4></summary>

  Please note that Waze is not reliable and could fail to fetch new travel times

  #### Setup 🛠️

  1. Install [Waze Travel Time](https://www.home-assistant.io/integrations/waze_travel_time/) integration through the UI: [Settings > Devices & services > Add integration > Waze Travel Time](https://my.home-assistant.io/redirect/config_flow_start/?domain=waze_travel_time)
  2. Apply the settings from below
  3. ⚠️ [Disable sensor auto-polling (steps 1, 2)](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval)
  4. Repeat steps 1-3 for each user

  #### Settings 🔧

  | Setting | Parameter |
  | :--- | :---: |
  | Name | `User0 Travel Time` |
  | Origin | `person.user0` |
  | Destination | `zone.home` *(your gate zone)* |
  | Region | Select your region |

</details>

<details>
  <summary><h4>Option 4: Smart vehicle 🌐</h4></summary>

  Some Home Assistant vehicle integrations or add-ons create a sensor that reports your remaining travel time

  To use this sensor in Automatic Gate, select `Listen for updates` for `Travel time refresh rate` in the `Travel time settings` inputs category

</details>


## Itinerary sensors 🗺️

Each input text helper stores user itinerary states and serves as a trigger for third-party automations

#### Setup 🛠️

1. Add an [input text helper](https://www.home-assistant.io/integrations/input_text/) through the UI: [Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Text
2. Apply the settings from below

#### Settings 🔧

| Setting | Parameter |
| :--- | :---: |
| Name | `User0 itinerary` |
| Icon | `mdi:map` |
| Minimum length | `0` |
| Maximum length | `255` |
| Display mode | `Text` |

> [!NOTE]
> Don't forget to set the maximum length to 255

#### Data stored 💾

<details>
  <summary><h5>Sensor JSON structure 🏗️</h5></summary>

| Key | Value |
| :---: | :---: |
| `status` | Holds the current Automatic Gate state for this user |
| `error` | Holds the error id if the Automatic Gate had to stop |
| `quick_triggers` | Holds the amount of time the Automatic Gate was triggered too quickly in a row for this user |
| `last_closed` | Holds the timestamp of the last time the Automatic Gate tried to close the gate |
| `auto_closed` | Holds if the Automatic Gate closed the gate with a timer or automatically, without an interaction from the user |

</details>

<details>
  <summary><h5>Possible status ℹ️</h5></summary>

| State | Meaning |
| :---: | :---: |
| `null` | The automation is not running for this user |
| `'leaving'` | The user is currently leaving home |
| `'arriving'` | The user is driving and being tracked by the automation |
| `'on_approach'` | The user has triggered the gate opening, and will arrive soon |

</details>

<details>
  <summary><h5>Possible errors 🚨</h5></summary>

| Error | Meaning |
| :---: | :---: |
| `null` | No error occurred |
| `'vehicle_stopped'` | The driver stopped his vehicle unexpectedly |
| `'canceling_order'` | The driver pressed the cancel itinerary button |
| `'did_not_leave'` | The driver did not leave home on time |
| `'did_not_arrive'` | The driver did not arrive home on time with the gate open |
| `'timed_out'` | The driver's phone did not report a new position in time |
| `'vehicle_away'` | The gate was waiting for an event to open upon departure, but the user left the activation zone |
| `'travel_time_did_not_respond'` | The travel time sensor did not update its value in time |
| `'not_home'` | The driver enabled the home presence check before opening, but was not detected at home |
| `'triggered_frequently'` | This driver triggered the blueprint multiple times too quickly |
| `'updated_frequently'` | The blueprint tried to update the travel time sensor too frequently and was stopped to prevent costs |
| `'forbidden_zone'` | The driver entered a forbidden zone upon arrival |
| `'invalid_travel_time_sensor'` | The travel time sensor provided does not exist |
| `'unsupported_tt_integration'` | The travel time sensor provided is not compatible with this blueprint |
| `'too_close'` | The driver started his vehicle in the activation zone, but outside his home |
| `'gate_closed'` | While waiting for the driver's location to be confirmed, the gate was manually opened and then closed |
| `'location_not_confirmed'` | The driver enabled the location request input, but the phone did not receive the request |
| `'got_no_gps_data'` | The phone received the location request but did not send back any GPS coordinates |

</details>

<details>
  <summary><h5>Automation examples 🔗</h5></summary>

  ###### Template code to retrieve itinerary sensor data

  ```jinja2
  {# EDIT THESE LINES #}
  {% set itinerary_sensor = 'input_text.itinerary_sensor' %}
  {% set attribute = 'status' %}
  {% set desired_state = none %}

  {%
    set default_itinerary_sensor_value = {
      "status": none,
      "error": none,
      "quick_triggers": 0,
      "last_closed": 0,
      "auto_closed": false
    }
  %}
  {{
    (
      states(itinerary_sensor)
      | from_json(default_itinerary_sensor_value)
    ).get(attribute) == desired_state
  }}
  ```

  ##### Trigger examples

  | Attribute | Desired state | Description |
  | :---: | :---: | :--- |
  | `status` | `['arriving', 'on_approach']` | Is true while the user is driving towards home |
  | `status` | `leaving` | Is true while the user is leaving and becomes false when the gate has been closed behind |
  | `error` | remove the `== desired_state` part | Triggers when an error occurs, contains the error code |

</details>


## Bluetooth transmitter 📡

Companion app BLE transmitter lets a scanner automatically close your gate upon leaving

The automation will automatically turn the transmitter off if not needed

> [!NOTE]
> Your Bluetooth transmitter should mark your devices as unavailable or away after a short time or this will have no effect

> [!WARNING]
> Please set the closing behavior to 'Notification request', or the gate could close on your vehicle if your ble tracker is unreliable

#### Setup 🛠️

1. Install through the [companion app](https://www.home-assistant.io/integrations/mobile_app/) settings: Settings > Companion app > Manage sensors > BLE Transmitter
2. Apply the settings from below

#### Settings 🔧

| Setting | Parameter |
| :--- | :---: |
| Advertise mode | - |
| Transmit only enabled on Home Wifi Network SSIDs | ❌ |
| Major | - |
| Measured power at 1 meter | - |
| Minor | - |
| Enable transmitter | - |
| Transmit power | - |
| UUID | [Random UUID](https://www.uuidgenerator.net/) |

> [!NOTE]
> Automatic Gate turns on the iBeacon itself with the right settings when needed if 'iBeacon transmitter entities' are provided


## Bluetooth entities 🔎

Each BLE tracker entity to monitor your distance from the gate while leaving, and close it when you're out of reach

Could be from my [ESPHome firmware](ESPHome-Firmwares/Gate) [configured](ESPHome-Firmwares/README.md#setup-ble-tracking-%EF%B8%8F), or any other BLE tracker near your gate

Supported types: device_tracker, rssi sensor, distance sensor, bermuda area sensor


## Bluetooth scanner switch ⏻

A switch which can turn on/off your BLE scanner. Not needed if your BLE scanner runs 24/7


## Nearest distance sensor 🤏

Only necessary for [ESPHome firmware](ESPHome-Firmwares/Gate)

Provides the distance of the nearest person to your gate, to open only if someone is close enough

#### Setup 🛠️

1. Install the [Proximity](https://www.home-assistant.io/integrations/proximity/) integration through the UI: [Settings > Devices & services > Add integration > Proximity](https://my.home-assistant.io/redirect/config_flow_start/?domain=proximity)
2. Apply the settings from below
3. Optional: Disable all sensors except `sensor.nearest_distance`

#### Settings 🔧

| Setting | Parameter |
| :--- | :---: |
| Track distance to | `zone.home` *(your gate zone)* |
| Devices or persons to track | `[person.user0, ...]` |
| Zones to ignore | - |
| Tolerance distance | - |
