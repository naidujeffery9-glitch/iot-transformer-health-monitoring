#define TEMP_PIN 34
#define CURRENT_PIN 35
#define RELAY_PIN 5

#define MAX_TEMP 80
#define MAX_CURRENT 20

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);
}

void loop() {
  int temp = analogRead(TEMP_PIN);
  int current = analogRead(CURRENT_PIN);

  if (temp > MAX_TEMP || current > MAX_CURRENT) {
    Serial.println("Transformer Fault Detected");
    digitalWrite(RELAY_PIN, LOW);
  }
  delay(2000);
}
