int value, index = 0, hundreds;
double brightness, media, mediaPrev, prevBrightness;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(2000000);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (index == 100) {
    mediaPrev = media / 100;
    hundreds = mediaPrev/100;
    //Serial.print(centinaia);
    //Serial.print("   ");
    if (hundreds <= 8) {
      brightness = 3.5*log10((hundreds) + 1) * 10;
    } else {
      brightness = 60;
    }
    if (brightness != prevBrightness) {
      Serial.println(int(brightness));
    }
    prevBrightness = brightness;
    media = 0;
    index = 0;
    delay(1000);
  } else {
    value = analogRead(A0);
    media += value;
    index++;
  }
  
}
