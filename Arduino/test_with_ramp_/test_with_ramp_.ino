
#include "AccelStepper.h"

#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38

AccelStepper stepper(1, X_STEP_PIN, X_DIR_PIN); // 1 = Driver

void setup() {
stepper.setMaxSpeed(400);
stepper.setAcceleration(50);

stepper.setEnablePin(X_ENABLE_PIN);
stepper.setPinsInverted(false, false, true); //invert logic of enable pin
stepper.enableOutputs();
}

void loop() {
stepper.runToNewPosition(0);

stepper.moveTo(500);
while (stepper.currentPosition() != 300)
stepper.run();

// cause an overshoot as we whiz past 300
stepper.setCurrentPosition(600);
}
