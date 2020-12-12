#include <ros.h>
#include <Arduino.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Point.h>
#include <AccelStepper.h>
#include <MultiStepper.h>


#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38


#define Y_STEP_PIN 60
#define Y_DIR_PIN 61
#define Y_ENABLE_PIN 56


#define Z_STEP_PIN 46
#define Z_DIR_PIN 48
#define Z_ENABLE_PIN 62

AccelStepper stepper1(1, X_STEP_PIN, X_DIR_PIN); 
AccelStepper stepper2(1, Z_STEP_PIN, Z_DIR_PIN);
AccelStepper stepper3(1, Y_STEP_PIN, Y_DIR_PIN);
MultiStepper steppers;

ros::NodeHandle nh;

void stepMotor1( const geometry_msgs::Point& msg){
    long positions[2]; // Array of desired stepper positions
    positions[0] = msg.x;
    positions[1] = msg.y;
    steppers.moveTo(positions);
    steppers.runSpeedToPosition();
    delay(1000); 
}


void place1(const std_msgs::Empty& toggle_msg){
    stepper1.move(100);
    stepper1.run();
    delay(1000); 
    stepper2.moveTo(200);
    stepper2.run();
    delay(1000); 
    stepper1.move(-100);
    stepper1.run();
    delay(1000); 
    stepper2.moveTo(0);
    stepper2.run();
    delay(1000); 
}
void take1(const std_msgs::Empty& toggle_msg){
    stepper2.moveTo(200);
    stepper2.run();
    delay(1000); 
    stepper1.move(100);
    stepper1.run();
    delay(1000); 
    stepper2.moveTo(0);
    stepper2.run();
    delay(1000); 
    stepper1.move(-100);
    stepper1.run();
    delay(1000); 
}



ros::Subscriber<geometry_msgs::Point> motor1("motor", &stepMotor1);
ros::Subscriber<std_msgs::Empty> placing("place", &place1);
ros::Subscriber<std_msgs::Empty> taking("take", &take1);


void setup() {
  // put your setup code here, to run once:

  stepper1.setMaxSpeed(1000.0);
  stepper1.setAcceleration(500.0);
  stepper1.setEnablePin(X_ENABLE_PIN);
  stepper1.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper1.enableOutputs();

  
  stepper2.setMaxSpeed(1000.0);
  stepper2.setAcceleration(500.0);
  stepper2.setEnablePin(Z_ENABLE_PIN);
  stepper2.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper2.enableOutputs();

  stepper3.setMaxSpeed(1000.0);
  stepper3.setAcceleration(500.0);
  stepper3.setEnablePin(Y_ENABLE_PIN);
  stepper3.setPinsInverted(false, false, true); //invert logic of enable pin
  stepper3.enableOutputs();
  
  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
  steppers.addStepper(stepper3);
  
  nh.initNode();
  nh.subscribe(motor1);
  nh.subscribe(placing);
  nh.subscribe(taking);

}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(1);
}
