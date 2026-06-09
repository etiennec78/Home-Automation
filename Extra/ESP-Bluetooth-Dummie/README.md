# ESP Bluetooth Dummie 🚗

## Description

A small Arduino sketch for an [ESP32](https://amzn.to/4kNCDHc) installed in your car so your phone detects it as a Bluetooth device and reports when you're driving

Useful if your car does not support Bluetooth, Android Auto, or CarPlay

## Installation Guide

### Setup

1. [Download Arduino IDE](https://www.arduino.cc/en/software)
2. Add ESP32 to your board library (Tools > Board > Board Manager > Install 'esp32 by Espressif Systems')
3. Download the latest version of [ESP32-BLE-Keyboard](https://github.com/T-vK/ESP32-BLE-Keyboard/releases)
4. Import the library (Sketch > Include Library > Add .ZIP Library...)
5. Go to File > Preferences and add `https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json` to 'Additional Boards Manager URLs'
6. Download and open [the script](esp-bluetooth-dummie.ino), and change the device name in the code
7. Plug your ESP32 into your computer
8. Click on "Select Board" and choose the corresponding ESP32 (If you don't know, select ESP32 Dev Module)
9. Click on the right arrow icon to upload your sketch to your ESP32
10. Pair the device with your phones via Bluetooth
11. Add an Android or iOS [template Bluetooth sensor](/sensors.md#driving-sensors-) in Home Assistant to detect when you are driving
