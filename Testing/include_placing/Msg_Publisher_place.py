import rospy
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
#include <std_msgs/Empty.h>

global msg
msg= Point()

def start():
    global pub
    global pub2
    rospy.init_node("motor", anonymous=True)
    pub = rospy.Publisher('motor',Point, queue_size=10)
    pub2 = rospy.Publisher('place',Empty,queue_size=10)

def A1():
    msg.x = 1000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def A2():
    msg.x = 2000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def A3():
    msg.x = 3000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def A4():
    msg.x = 4000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def B1():
    msg.x = 1000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def B2():
    msg.x = 2000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def B3():
    msg.x = 3000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def B4():
    msg.x = 4000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def C1():
    msg.x = 1000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def C2():
    msg.x = 2000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def C3():
    msg.x = 3000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def C4():
    msg.x = 4000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def D1():
    msg.x = 1000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def D2():
    msg.x = 2000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def D3():
    msg.x = 3000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def D4():
    msg.x = 4000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def E1():
    msg.x = 1000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def E2():
    msg.x = 2000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def E3():
    msg.x = 3000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def E4():
    msg.x = 4000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()

if __name__=='__main__':
    try:
        start()
    except rospu.ROSInterruptException:
        pass
