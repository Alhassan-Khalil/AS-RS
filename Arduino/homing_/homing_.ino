
#include <AccelStepper.h>
#include <MultiStepper.h>

#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38


#define Z_STEP_PIN 46
#define Z_DIR_PIN 48
#define Z_ENABLE_PIN 62

AccelStepper stepper1(1, X_STEP_PIN, X_DIR_PIN); 
AccelStepper stepper2(1, Z_STEP_PIN, Z_DIR_PIN);

// Define the Pins used
#define home_switch 32
#define home_switch2 47

// Stepper Travel Variables
long initial_homing=-1;  // to Home Stepper at startup


void setup() {   
   pinMode(home_switch, INPUT_PULLUP);
   pinMode(home_switch2, INPUT_PULLUP);
   delay(5); 

   //  Set Max Speed and Acceleration of each Steppers at startup for homing
  stepper1.setMaxSpeed(100.0);      // Set Max Speed of Stepper (Slower to get better accuracy)
  stepper1.setAcceleration(100.0);  // Set Acceleration of Stepper
  stepper1.setEnablePin(X_ENABLE_PIN);
  stepper1.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper1.enableOutputs();
  stepper2.setMaxSpeed(100.0);
  stepper2.setAcceleration(100.0);
  stepper2.setEnablePin(Z_ENABLE_PIN);
  stepper2.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper2.enableOutputs();
  

// Start Homing procedure of Stepper Motor at startup

  while (digitalRead(home_switch)) {  // Make the Stepper move CCW until the switch is activated   
    stepper1.moveTo(initial_homing);  // Set the position to move to
    //stepper2.moveTo(initial_homing);
    initial_homing--;  // Decrease by 1 for next move if needed
    stepper1.run();  // Start moving the stepper
//  stepper2.run();
    delay(5);
}

  while (digitalRead(home_switch2)) {  // Make the Stepper move CCW until the switch is activated   
    //stepper1.moveTo(initial_homing);  // Set the position to move to
    stepper2.moveTo(initial_homing);
    initial_homing--;  // Decrease by 1 for next move if needed
    //stepper1.run();  // Start moving the stepper
    stepper2.run();
    delay(5);
}


  stepper1.setCurrentPosition(0);  
//  stepper1.setMaxSpeed(100.0);      
//  stepper1.setAcceleration(100.0);
  stepper2.setCurrentPosition(0);  
//  stepper2.setMaxSpeed(100.0);      
//  stepper2.setAcceleration(100.0); 
  initial_homing=1;

  while (!digitalRead(home_switch)) { // Make the Stepper move CW until the switch is deactivated
    stepper1.moveTo(initial_homing);  
    stepper1.run();
    stepper2.moveTo(initial_homing);  
    stepper2.run();
    initial_homing++;
    delay(5);
  }
  
  while (!digitalRead(home_switch2)) { // Make the Stepper move CW until the switch is deactivated
    //stepper1.moveTo(initial_homing);  
    //stepper1.run();
    stepper2.moveTo(initial_homing);  
    stepper2.run();
    initial_homing++;
    delay(5);
  }
  
  stepper1.setCurrentPosition(0);
  stepper1.setMaxSpeed(1000.0);      // Set Max Speed of Stepper (Faster for regular movements)
  stepper1.setAcceleration(1000.0);  // Set Acceleration of Stepper
    stepper2.setCurrentPosition(0);
  stepper2.setMaxSpeed(1000.0);      // Set Max Speed of Stepper (Faster for regular movements)
  stepper2.setAcceleration(1000.0);  // Set Acceleration of Stepper
  //--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  //--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
}

void loop() {

}
