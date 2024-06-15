# Esphome Phillips LivingColors firmware 💡

## Description 📝

A simple ESPHome configuration to hack a Phillips LivingColors Mini with an ESP32

Has both E1.31 and WLED protocols enabled by default for light software control (e.g.: [Artemis](https://github.com/Artemis-RGB/Artemis))

## How to Install 🚀

### Prerequisites 📝

1. An [ESP32](https://amzn.to/44BPk0g)
2. [ESPHome installed](https://esphome.io/guides/installing_esphome.html)
3. Pins +, -, R, G, B from the led controller soldered onto the ESP32 as shown in [this tutorial](https://thewerner.medium.com/a-brain-for-the-light-c5b290c2e31a)

### Steps 📜

1. Clone this repo
    * Run : `git clone https://github.com/etiennec78/Home-Automation.git`
2. Edit [the file](livingcolors.yaml) to fill your needs
    * Change GPIO pins
    * Replace any "!secret" line with your own information
    * Remove E1.31 or WLED if you don't need them
3. Flash your ESP32
    * Plug it into your computer
    * Run : `python -m esphome run livingcolors.yaml`
4. Connect your ESP32 to Home Assistant
    * Home Assistant should detect your ESPHome device automatically on your LAN
    * Connect it and enter your api_key

## Pictures 📷

|       |       |       |
| :---: | :---: | :---: |
| <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Esphome%20Phillips%20LivingColors/livingcolors1.jpg?raw=true" width="100%" alt="First lamp components view" > | <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Esphome%20Phillips%20LivingColors/livingcolors2.jpg?raw=true" width="100%" alt="Second lamp components view"> | <img src="https://github.com/etiennec78/etiennec78.github.io/blob/main/media/Home%20Automation/Esphome%20Phillips%20LivingColors/livingcolors3.jpg?raw=true" width="100%" alt="Third lamp components view"> |
