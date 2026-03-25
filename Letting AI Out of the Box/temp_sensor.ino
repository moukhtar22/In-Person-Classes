#include <SPI.h>
#include <WiFiNINA.h>
#include "DHT.h"

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // Change to DHT22 if using that sensor
DHT dht(DHTPIN, DHTTYPE);

const int sensorPin = A0;
const int fanPin = 3;

char ssid[] = "Wahwahwest";       
char pass[] = "4104871265";    
int status = WL_IDLE_STATUS;

char server[] = "crappy-ai.com";    // Replace with your server URL
WiFiClient client;

void setup() {
  Serial.begin(9600);
  pinMode(fanPin, OUTPUT);
  
  // Attempt to connect to WiFi network
  while (status != WL_CONNECTED) {
    Serial.print("Connecting to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }
  Serial.println("Connected!");
}

void loop() {

  // 1. Read the analog sensor
  int reading = analogRead(sensorPin);
  
  // 2. Convert to Voltage (assuming 5V board)
  float voltage = reading * 5.0;
  voltage /= 1024.0; 
  
  // 3. Convert to Celsius (10mV per degree with 500mV offset)
  float temperatureC = (voltage - 0.5) * 100 ;
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
  
  Serial.print("Raw: "); Serial.print(reading);
  Serial.print(" | Temp: "); Serial.println(temperatureF);

  // 4. Send to Server
  getData(temperatureF);

  String webValue = getFromServer();
  
  if (webValue != "") {
    Serial.print("Value from Web: ");
    Serial.println(webValue);
  }

  if (webValue == "on") {
      digitalWrite(fanPin, HIGH); // Turn LED ON
      Serial.println("Fan Turned On");
    } else {
      digitalWrite(fanPin, LOW);  // Turn LED OFF
      Serial.println("Fan Turned Off");
    }
  
  delay(5000); // 10 second intervals
}

void getData(float value) {
  if (client.connect(server, 80)) {
    Serial.println("Connecting for GET...");

    // Construct the URL with the data: /temp?temp=42
    // The "temp=" part matches request.forms.get('temp') or request.query.get('temp')
    client.print("GET /temp?temp=");
    client.print(value);
    client.println(" HTTP/1.1");
    
    client.print("Host: ");
    client.println(server);
    client.println("Connection: close");
    client.println(); // Every HTTP request must end with a blank line

    Serial.print("Sent GET with value: ");
    Serial.println(value);

    // Check for a response from the server
    while (client.connected() || client.available()) {
      if (client.available()) {
        char c = client.read();
        Serial.print(c);
      }
    }
    client.stop();
  } else {
    Serial.println("Connection failed");
  }
}

String getFromServer() {
  String result = "";


if (client.connect(server, 80)) {
    Serial.println("Connecting to fetch value...");
    
    // Send the GET request
    client.println("GET /command HTTP/1.1");
    client.print("Host: ");
    client.println(server);
    client.println("Connection: close");
    client.println(); // End of headers

    // 1. Skip the HTTP Headers
    // We look for the blank line (\r\n\r\n) that separates headers from body
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") { // This indicates the end of headers
        break;
      }
    }

    // 2. Read the remaining data (The Body)
    while (client.available()) {
      char c = client.read();
      result += c;
    }
    client.stop();
  } else {
    Serial.println("Fetch failed");
  }
  
  return result;
}
