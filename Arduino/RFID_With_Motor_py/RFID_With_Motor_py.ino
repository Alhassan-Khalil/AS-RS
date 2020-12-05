#include <ros.h>
#include <Arduino.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Point.h>
//motors lib
#include <AccelStepper.h>
#include <MultiStepper.h>
//RFID lib
#include <SPI.h>
#include <RFID.h>

//rfid define
#define SS_PIN 10
#define RST_PIN 9

RFID rfid(SS_PIN, RST_PIN);


#define X_STEP_PIN 54
#define X_DIR_PIN 55
#define X_ENABLE_PIN 38

#define Z_STEP_PIN 46
#define Z_DIR_PIN 48
#define Z_ENABLE_PIN 62

AccelStepper stepper1(1, X_STEP_PIN, X_DIR_PIN); 
AccelStepper stepper2(1, Z_STEP_PIN, Z_DIR_PIN);
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


ros::Subscriber<geometry_msgs::Point> motor1("motor", &stepMotor1);




void RFID(){
  String rfidCard;
   //Check if any RFID Tags Detected or not?
  if(rfid.isCard()){
    //if RFID Tag is detected, check for the Unique ID,
    if(rfid.readCardSerial()){
       rfidCard = String(rfid.serNum[0]) + " " + String(rfid.serNum[1]) + " " + String(rfid.serNum[2]) + " " + String(rfid.serNum[3]);
       if (rfidCard =="34 103 107 52"){
        long positions[2];
        positions[0] = 1000;
        positions[1] = 1000;
        steppers.moveTo(positions);
        steppers.runSpeedToPosition();
        delay(1000);}
        else if (rfidCard =="233 16 216 86"){
        long positions[2];
        positions[0] = 2000;
        positions[1] = 2000;
        steppers.moveTo(positions);
        steppers.runSpeedToPosition();
        delay(1000);}
       else if (rfidCard =="57 154 26 43"){
        long positions[2];
        positions[0] = 3000;
        positions[1] = 3000;
        steppers.moveTo(positions);
        steppers.runSpeedToPosition();
        delay(1000);}
       else if (rfidCard =="217 83 102 194"){
        long positions[2];
        positions[0] = 4000;
        positions[1] = 4000;
        steppers.moveTo(positions);
        steppers.runSpeedToPosition();
        delay(1000);}
    }
    rfid.halt();
  }
  
}




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


  SPI.begin();
  rfid.init();
  
  // Then give them to MultiStepper to manage
  steppers.addStepper(stepper1);
  steppers.addStepper(stepper2);
  
  nh.initNode();
  nh.subscribe(motor1);
}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(1);
}
