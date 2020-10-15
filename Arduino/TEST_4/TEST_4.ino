#include <ros.h>
#include <Arduino.h>
#include <std_msgs/Empty.h>
#include <std_msgs/Float32.h>
#include <AccelStepper.h>



AccelStepper stepper1(4, 9, 10, 11, 12); 

ros::NodeHandle nh;


void stepMotor1 (const std_msgs::Float32 & rpm){
    stepper1.moveTo(rpm.data);
    stepper1.runToPosition();
    //char log_msg[20];
    //sprintf(log_msg,"data: &d",(int)rpm.data);
    //nh.loginfo(log_msg);
    //nh.loginfo(".....");
    delay(1000);
}


ros::Subscriber<std_msgs::Float32> motor1("motor1/start", &stepMotor1);


void setup() {
  // put your setup code here, to run once:

  stepper1.setMaxSpeed(500.0);
  stepper1.setAcceleration(100.0);

  nh.initNode();
  nh.subscribe(motor1);
}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(1);
}
