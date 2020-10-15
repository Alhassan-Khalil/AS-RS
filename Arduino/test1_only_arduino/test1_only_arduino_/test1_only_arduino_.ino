#define pwr 1
#define xDir 5 // X axies dir pin
#define xstep 2 // X axis step pin

int steps = 3200; // steps to move og 6400 , 200 step per rev
int stepdelay = 60; // Delay between eacg pause og 30


void rotate(boolean dir , byte dirPin, byte stepperPin, int steps)
{
  digitalWrite(dirPin, dir);
  delay(100);
  for (int i = 0; 1 < steps; i++) {
    digitalWrite(stepperPin,HIGH);
    delayMicroseconds(stepdelay);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(stepdelay);
  }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(xDir,OUTPUT);
  pinMode(xstep,OUTPUT);
  pinMode(pwr,OUTPUT);
  digitalWrite(pwr,LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  rotate(false , xDir, xstep , 800); //X axis rotate clockwise
  delay(2000);
  rotate(true , xDir, xstep , 800);// X axis rotate clock wise 
  delay(2000);
}
