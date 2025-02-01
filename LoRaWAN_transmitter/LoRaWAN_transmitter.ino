#include <MKRWAN.h>
#include "arduino_secrets.h"

LoRaModem modem;

String appEui = SECRET_APP_EUI;
String appKey = SECRET_APP_KEY;

void setup() {

  Serial.begin(115200);
  while (!Serial);
  // change this to your regional band (eg. US915, AS923, ...)
  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}
  };
  
  modem.setADR(true);

  // connect to TTN
  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry");
    while (1) {}
  }

  Serial.print("- Current mask: ");
  Serial.println(modem.getChannelMask());


  // Set poll interval to 60 secs.
  modem.minPollInterval(60);
  // NOTE: independent of this setting, the modem will
  // not allow sending more than one message every 2 minutes,
  // this is enforced by firmware and can not be changed.
}

void loop() {
  
  Serial.println();
  Serial.println("Enter a message to send to network");

  while (!Serial.available());
  String msg = Serial.readStringUntil('\n');

  Serial.println();
  Serial.print("Sending");

  Serial.println();
  int err;
  modem.beginPacket();
  modem.print(msg);
  err = modem.endPacket(true);
  if (err > 0) {
    Serial.println("Message sent correctly!");
  } else {
    Serial.println("Error sending message :");
    Serial.println("(you may send a limited amount of messages per minute, depending on the signal strength");
    Serial.println("it may vary from 1 message every couple of seconds to 1 message every minute)");
  }
  delay(1000);
}
