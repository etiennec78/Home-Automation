# Description 📝

* Sensors used in Automatic Gate [blueprint](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate), [automations](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Automations), [frontend](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Frontend), and [gate firmware](https://github.com/etiennec78/Home-Automation/tree/master/Automatic%20Gate/Extra/Esphome%20gate%20firmware)
* Prefer installing sensors through the UI when possible
* Replace user0 with your real name
* Some sensors require to be set for each user


# Required sensors 📌

## Gate ⛩️

**The switch or cover which controls your gate**

Could be from my [esphome firmware](Extra/Esphome%20gate%20firmware/gate.yaml) or any other integration


## GPS location trackers 🌎

**Each GPS location tracker necessary to detect if you're in your leaving/arriving, estimate your travel time, and track your distance**

*Notes :*

* *⚠️ Use high precision while driving in your ETA calculation zone or you could time out*
* *If your location tracker has report latency (wifi/ble), and you plug Android Auto just after leaving, your gate could open thinking you are still there*
* *If high precision mode does not trigger, please increase its range (try 2500m if you don't use Android Auto)*

Install through [companion app](https://companion.home-assistant.io/docs/core/location/) settings : *Settings > Companion app > Manage sensors > Background location ✔*

Settings :

* High accuracy mode : ✔
* High accuracy mode only when connected to BT devices : Select vehicles bluetooth devices
* High accuracy mode only when entering zone : `zone.home` *(or another zone if your gate is not at home)*
* High accuracy mode trigger range for zone : The range in which you want your phone to spam location updates when arriving (suggested : 1000m)
* High accuracy interval : `5s`
* High accuracy mode only when connected to BT devices : ✔
* Minimal precision : Keep default
* Location sent : `Exact`

Then, assign these device trackers to each person by going into : *[Settings > People](https://my.home-assistant.io/redirect/people/) > Select a user > Track devices > Your new device tracker*


## Driving sensors 🚗

**Each driving sensor which will detect when you start and stop driving**

Either Android Auto, bluetooth connexion, or both grouped

### Option 1 : Android Auto connection

Install through [companion app](https://companion.home-assistant.io/docs/core/sensors#android-auto) settings : *Settings > Companion app > Manage sensors > Android Auto ✔*

### Option 2 : Bluetooth connection with template sensor

Install through [companion app](https://companion.home-assistant.io/docs/core/sensors/#bluetooth-sensors) settings : *Settings > Companion app > Manage sensors > Bluetooth connection ✔*

Install a [template helper](https://www.home-assistant.io/integrations/template/) through the UI : *[Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Template > Binary sensor*

Settings :

* Name : `User0 driving`
* State template : `{{ '00:00:00:00:00:00 (BT-Device)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}`
* Device class : `Moving`

Or in your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file :

```yaml
template:
  - binary_sensor:
    - name: "user0 driving"
      unique_id: "user0_driving"
      icon: mdi:steering
      device_class:  moving
      state: >
        {{ '00:00:00:00:00:00 (BT-Device)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}
```

*Note : If your vehicle repeatedly cuts the USB power supply during engine start-up, you should add `delay_off: 00:00:03` in binary_sensor attributes (e.g, after state:)*

* `00:00:00:00:00:00:00` is your vehicle mac address
* `Bt-Device` is the device name of your vehicle
* `sensor.user0_bluetooth_connection` is your bluetooth companion sensor
* `connected_paired_devices` needs to be left untouched

### Option 3 : Both (for multiple vehicles)

Install sensors from options 1 & 2

Then use the following template : `{{ is_state('binary_sensor.user0_android_auto', 'on') or '00:00:00:00:00:00 (BT-Device)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}`


## Travel time sensors ✈️

**Each travel time sensor monitoring each user time left before arrival**

### Option 1 : Waze

**⚠️ Please disable [auto-polling](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval)**

Install [Waze Travel Time](https://www.home-assistant.io/integrations/waze_travel_time/) integration through the UI : *[Settings > Devices & services > Add integration > Waze Travel Time](https://my.home-assistant.io/redirect/config_flow_start/?domain=waze_travel_time)*

Install the integration multiple times if you have multiple users

Settings :

* Name : `User0 Travel Time`
* Origin : `person.user0`
* Destination : `zone.home` *(or another zone if your gate is not at home)*
* Region : Select your region

### Option 2 : Google Maps

**⚠️ Please disable [auto-polling](https://www.home-assistant.io/integrations/waze_travel_time/#defining-a-custom-polling-interval)**

⚠️ Work in progress ! The current integration is not reporting usable attributes

Install [Google Maps Travel Time](https://www.home-assistant.io/integrations/google_travel_time/) integration through the UI : *[Settings > Devices & services > Add integration > Google Maps Travel Time](https://my.home-assistant.io/redirect/config_flow_start/?domain=google_travel_time)*

Install the integration multiple times if you have multiple users

* Name : `User0 Travel Time`
* API key : Your api key
* Origin : `person.user0`
* Destination : `zone.home` *(or another zone if your gate is not at home)*


## Proximity sensors 📏

**Each proximity sensor which calculates the distance of each user from your gate**

Delivered by the

Install the [Proximity](https://www.home-assistant.io/integrations/proximity/) integration through the UI : *[Settings > Devices & services > Add integration > Proximity](https://my.home-assistant.io/redirect/config_flow_start/?domain=proximity)*

Settings :

* Track distance to : `zone.home` *(or another zone if your gate is not at home)*
* Devices or persons to track : `[person.user0, ...]`
* Zones to ignore : `[]`
* Tolerance distance : Not required by Automatic Gate


## Notify services 💬

**Each phone notification service to notify of the itinerary status**

Delivered by the [companion app](https://companion.home-assistant.io/docs/notifications/notifications-basic) by default

Find the service ids by going into : *[Developer tools > Services tab](https://my.home-assistant.io/redirect/developer_states/) > searching for "notify."*


## Itinerary sensors 🗺️

**Each empty itinerary input text helper to store each user itinerary state**

Install an [input text helper](https://www.home-assistant.io/integrations/input_text/) through the UI : *[Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Text*

Settings :

* Name : `User0 itinerary`
* Icon : `mdi:map`
* Minimum lenght : `0`
* Maximum length : `100`
* Display mode : `Text`

Or in your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file :

```yaml
input_text:
  user0_itinerary:
    name: User0 itinerary
    initial: none
    icon: mdi:map
```

## Planned opening 📅

**An empty input datetime helper which will be used to set an ETA and plan the opening of your gate**

Install an [input datetime helper](https://www.home-assistant.io/integrations/input_datetime/) through the UI : *[Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Date and/or time*

Settings :

* Name : `Automatic gate planned opening`
* What do you want to input : `Date and time`

Or in your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file :

```yaml
input_datetime:
  planned_opening:
    name: Automatic gate planned opening
    has_date: true
    has_time: true
```



# Optional sensors ➕

## Bluetooth transmitter 📡

**Companion app ble transmitter to let a scanner automatically close your gate upon leaving**

The automation will automatically turn the transmitter off if not needed

*Notes :*

* *Your bluetooth transmitter should report your devices unavailable after a small time period or this won't have any effect*
* *Be aware that having your BLE transmitter too far away from your gate could make your gate close onto your car when the signal is lost before leaving*
* *The transmitter should be set to off by default since this blueprint will automatically turn it on when needed*

Install through [companion app](https://www.home-assistant.io/integrations/mobile_app/) settings : *Settings > Companion app > Manage sensors > BLE Transmitter ✔*

Settings :

* Advertise mode : `Low latency (10Hz)`
* Transmit only enabled on Home Wifi Network SSIDs : ✖
* major : `100`
* Measured power at 1 meter : Not necessary for Automatic Gate
* minor : `1`
* Enable transmitter : ✖
* Transmit power : `High`
* UUID : A [random UUID](https://www.uuidgenerator.net/)

## Bluetooth entities 🔎

**Each BLE rssi tracker entity to monitor your distance from the gate while leaving, to close it when you're out of reach**

Could be from my [esphome firmware](Extra/Esphome%20gate%20firmware) or any other bluetooth iBeacon scanner near your gate

## Bluetooth scanner switch ⏻

**A switch which can turn on/off your BLE scanner. Not useful if you want your BLE scanner running 24/7**

## Last notification 🔔

Only necessary for itinerary tracker notification [automation](Extra/Automations)

**An empty input datetime helper which will store the last time a tracking notification was sent to your devices**

Install an [input datetime helper](https://www.home-assistant.io/integrations/input_datetime/) through the UI : *[Settings > Devices & services > Helpers tab](https://my.home-assistant.io/redirect/helpers/) > Create helper > Date and/or time*

Settings :

* Name : `Last notification`
* Icon : `mdi:bell`
* What do you want to input : `Date and time`

Or in your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file :

```yaml
input_datetime:
  planned_opening:
    name: Last notification
    icon : mdi:bell
    has_date: true
    has_time: true
```

Then you may mute this sensor by adding this line to your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file

```yaml
logbook:
  exclude:
    entities:
      - input_datetime.last_notification
```

## Notify all devices group 🔔

**A group which allows my [esphome firmware](Extra/Esphome%20gate%20firmware) to notify all users in case of an event like your gate opening**

Install a [notification group](https://www.home-assistant.io/integrations/group/#notify-groups) in your [configuration.yaml](https://www.home-assistant.io/docs/configuration/) file :

```yaml
notify:
  platform: group
  name: "All devices"
  services:
    - service: mobile_app_user0_phone
    - ...
```

## Nearest distance sensor 🤏

Only necessary for [esphome firmware](Extra/Esphome%20gate%20firmware)

**Gives the distance of the nearest person from your gate, to only open if someone is close enough**

To install, please follow the instructions for the [required proximity sensors](sensors.md#proximity-sensors-)
