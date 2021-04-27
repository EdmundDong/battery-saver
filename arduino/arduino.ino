int relayPin = 13;
int op;
int light;

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  /*
   * Get operation for relay from serial
   */
  if (Serial.available() == 0)
    return; // return if no command from serial
  light = Serial.parseInt(); // get command from serial
  Serial.readString(); // throw away garbage
  /*
   * Activate/Deactivate LED and relay
   */
  if (light == 0) {
    digitalWrite(LED_BUILTIN, 0);
    digitalWrite(relayPin, 1); // relay is set to normally closed
  } else {
    digitalWrite(relayPin, 0); // relay is set to normally closed
    digitalWrite(LED_BUILTIN, 1);
  }
  /*
   * Give feedback to serial
   */
  Serial.println(light);
}
