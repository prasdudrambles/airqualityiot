#include <ESP8266WiFi.h>
#include <ThingSpeak.h>

// WiFi settings
const char* ssid = "your_SSID_here";
const char* password = "your_PASSWORD_here";

// ThingSpeak settings
unsigned long channelID = your_channel_ID_here;
const char* writeAPIKey = "your_write_API_key_here";
const char* server = "api.thingspeak.com";

// Gas sensor settings
int sensorValue = 0;
int airQualityIndex = 0;
int samplingTime = 280;
int deltaTime = 40;
int pin = A0;

void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  // Initialize ThingSpeak
  ThingSpeak.begin(client);
}

void loop() {
  // Read analog value from gas sensor
  sensorValue = analogRead(pin);
  
  // Calculate air quality index
  float Rs = 1023.0 / (float)sensorValue - 1.0;
  float ratio = Rs / (float)(samplingTime * 9.8);
  airQualityIndex = 0.25 * ratio * 10000 / (5.0 - ratio);

  // Print air quality index
  Serial.print("Air Quality Index: ");
  Serial.println(airQualityIndex);

  // Update ThingSpeak channel
  ThingSpeak.writeField(channelID, 1, airQualityIndex, writeAPIKey);

  // Wait for 15 seconds before taking another reading
  delay(15000);
}
