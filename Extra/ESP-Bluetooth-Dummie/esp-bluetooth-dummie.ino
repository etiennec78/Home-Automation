#include <BleKeyboard.h>
#define USE_NIMBLE

BleKeyboard bleKeyboard;

void setup() {
  bleKeyboard.setName("Vehicle");
  bleKeyboard.begin();
}

void loop() {
}
