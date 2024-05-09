# Ble car device 🚗
## Description 📝
A really small Arduino code to let a ESP32 sit in your car and show up as a BLE device so that your phone can connect to it and monitor if you are in your car

## How to install 🚀
1. [Download Arduino IDE](https://www.arduino.cc/en/software)
2. Add ESP32 in your device library (Tools > Board > Board Manager > Install esp32 by Espressif Systems)
3. Download the latest version of [ESP32-BLE-Keyboard](https://github.com/T-vK/ESP32-BLE-Keyboard/releases)
4. Import the library (Sketch > Include Library > Add .ZIP Library...)
5. Open the script and change the device name
6. Plug your ESP32 into your computer
7. Click on the right arrow icon to upload your sketch to your ESP32
8. Add a template sensor in Home Assistant to detect when you are driving, either from the UI (Settings > Devices > Helpers > Add a helper > Template > Binary) or your config

UI tempate
```yaml
{{ '00:00:00:00:00:00 (Vehicle)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}
```
Config template
```yaml
template:
  - binary_sensor:
      - name: "user0 driving"
        unique_id: "user0_driving"
        icon: mdi:steering
        device_class:  moving
        state: >
          {{ '00:00:00:00:00:00 (Vehicle)' in state_attr('sensor.user0_bluetooth_connection', 'connected_paired_devices') }}
```