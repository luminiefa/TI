#define BP 8

boolean etatBpAncien = false;

void setup() {
    Serial.begin(9600);
    pinMode(BP, INPUT_PULLUP);
}
    
void loop() {
    boolean etatBp =! digitalRead(BP);
    if(etatBp != etatBpAncien) {
        if (etatBp) {
            Serial.println("Bouton enfoncé");
        } else {
            Serial.println("Bouton laché");
        }
    }
    etatBpAncien = etatBp;
}