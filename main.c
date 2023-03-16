//library links in pseudocode

#include <ESP8266WiFi.h>
#include <ThingSpeak.h>

//Access point credentials
//point to a different file for security reasons
const char* ssid = "AP_ssid";
const char* password = "AP_password";

//initializing thingspeak API
unsigned long channelID = your_channel_ID_here;
const char* writeAPIKey = "API_key";
const char* server = "api.thingspeak.com";

// initial MQ-135 settings
int sensorValue = 0;
int airQualityIndex = 0;
int samplingTime = 280;
int deltaTime = 40;
int pin = A0;

void setup() {
  Serial.begin(115200);

  //connect to AP
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  //thingspeak api
  ThingSpeak.begin(client);
}

void loop() {
  //Read analog value from gas sensor
  sensorValue = analogRead(pin);
  
  // Calculation of AQI
  float Rs = 1023.0 / (float)sensorValue - 1.0;
  float ratio = Rs / (float)(samplingTime * 9.8);
  airQualityIndex = 0.25 * ratio * 10000 / (5.0 - ratio);

  //AQI
  Serial.print("Air Quality Index: ");
  Serial.println(airQualityIndex);
  //sync with thingspeak
  ThingSpeak.writeField(channelID, 1, airQualityIndex, writeAPIKey);
  delay(15000);
}
