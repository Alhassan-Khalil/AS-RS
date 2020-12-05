#include <ros.h>
#include <Arduino.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Point.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
//-------Motor x ------
#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38
//-------Motor z or y ---
#define Z_STEP_PIN 46
#define Z_DIR_PIN 48
#define Z_ENABLE_PIN 62
//------Home Switch-----
#define home_switch 32
#define home_switch2 47
long initial_homing=-1;  // to Home Stepper at startup

AccelStepper stepper1(1, X_STEP_PIN, X_DIR_PIN); 
AccelStepper stepper2(1, Z_STEP_PIN, Z_DIR_PIN);
MultiStepper steppers;

ros::NodeHandle nh;

void Homing(){
  stepper1.setMaxSpeed(100.0);      // Set Max Speed of Stepper (Slower to get better accuracy)
  stepper1.setAcceleration(100.0);  // Set Acceleration of Stepper
  stepper2.setMaxSpeed(100.0);
  stepper2.setAcceleration(100.0);

  while (digitalRead(home_switch)) {  // Make the Stepper move CCW until the switch is activated   
    stepper1.moveTo(initial_homing);  // Set the position to move to
    initial_homing--;  // Decrease by 1 for next move if needed
    stepper1.run();  // Start moving the stepper
    delay(5);
    }
  while (digitalRead(home_switch2)) {  // Make the Stepper move CCW until the switch is activated   
    stepper2.moveTo(initial_homing);
    initial_homing--;
    stepper2.run();
    delay(5);
    }
  stepper1.setCurrentPosition(0);  
  stepper2.setCurrentPosition(0);
    
  while (!digitalRead(home_switch)) { // Make the Stepper move CW until the switch is deactivated
    stepper1.moveTo(initial_homing);  
    stepper1.run();
    initial_homing++;
    delay(5);
  }
  
  while (!digitalRead(home_switch2)) { // Make the Stepper move CW until the switch is deactivated
    stepper2.moveTo(initial_homing);  
    stepper2.run();
    initial_homing++;
    delay(5);
  }
  stepper1.setCurrentPosition(0);  
  stepper2.setCurrentPosition(0);
}
//-------------------------------------------------------------

void stepMotor1( const geometry_msgs::Point& msg){
    long positions[2]; // Array of desired stepper positions
    positions[0] = msg.x;
    positions[1] = msg.y;
    steppers.moveTo(positions);
    steppers.runSpeedToPosition();
    delay(1000); 
}

ros::Subscriber<geometry_msgs::Point> motor1("motor1/start", &stepMotor1);

void setup() {
  // put your setup code here, to run once:
  pinMode(home_switch, INPUT_PULLUP);
  pinMode(home_switch2, INPUT_PULLUP);
  delay(5);
  
  stepper1.setEnablePin(X_ENABLE_PIN);
  stepper1.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper1.enableOutputs();
  stepper2.setEnablePin(Z_ENABLE_PIN);
  stepper2.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper2.enableOutputs();

    nh.initNode();
  nh.subscribe(motor1);
  // calling homing funcation
  Homing();
   
  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(500.0);
  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(500.0);
  
  
  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
//  
//  nh.initNode();
//  nh.subscribe(motor1);
}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(1);
}
