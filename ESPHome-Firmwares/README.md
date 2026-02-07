# ESPHome Firmwares ⚙️

| Firmware | Description | File |
| :---: | :---: | :---: |
| Gate ⛩️ | [Read More](ESPHome-Firmwares/Gate) | [File](ESPHome-Firmwares/Gate/gate.yaml) |
| Philips LivingColors 💡 | [Read More](ESPHome-Firmwares/Philips-LivingColors) | [File](ESPHome-Firmwares/Philips-LivingColors/livingcolors.yaml) |
| Velux Shutter 🪟 | [Read More](ESPHome-Firmwares/Velux-Shutter) | [File](ESPHome-Firmwares/Velux-Shutter/velux-shutter.yaml) |

### Setup BLE tracking 🛠️

All of these ESPHome firmware come with the [Bluetooth Proxy](https://esphome.io/components/bluetooth_proxy/) component

If you want to track your BLE devices, I recommend using either [Bermduda](https://github.com/agittins/bermuda) or [iBeacon](https://www.home-assistant.io/integrations/ibeacon/) integrations

<details>
  <summary>Bermuda</summary>
  
  1. Add your ESPHome device to Home Assistant
  2. Make sure you have [HACS](https://hacs.xyz/) installed
  3. Click [here](https://my.home-assistant.io/redirect/hacs_repository/?owner=agittins&repository=bermuda&category=Integration) to download the integration
  4. Restart Home Assistant
  5. [Add](https://my.home-assistant.io/redirect/config_flow_start/?domain=bermuda) the integration
  6. Go to your [Bermuda integration pannel](https://my.home-assistant.io/redirect/integration/?domain=bermuda) and click on the cog next to the main device
  7. Click on `Select devices` then `Configured devices` and find your device
  8. A new device will be created with sensors like distance, room, floor, etc...
    
</details>

<details>
  <summary>iBeacon</summary>
  
  1. [Add](https://my.home-assistant.io/redirect/config_flow_start/?domain=ibeacon) the integration
  2. If your iBeacon transmitter has a UUID (like the Android transmitter)
      1. Go to your [iBeacon integration pannel](https://my.home-assistant.io/redirect/integration/?domain=ibeacon)
      2. Click on the cog next to the main device
      3. Add your iBeacon transmitter UUID

</details>
