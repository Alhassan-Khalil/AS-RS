import rospy
from geometry_msgs.msg import Point, Twist

global msg
msg= Point()

def start():
    global pub
    rospy.init_node("motor", anonymous=True)
    pub = rospy.Publisher('motor',Point, queue_size=10)

def A1():
    msg.x = 2000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def A2():
    msg.x = 3000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def A3():
    msg.x = 4000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def A4():
    msg.x = 5000
    msg.y = 1000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B1():
    msg.x = 2000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B2():
    msg.x = 3000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B3():
    msg.x = 4000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B4():
    msg.x = 5000
    msg.y = 2000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C1():
    msg.x = 2000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C2():
    msg.x = 3000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C3():
    msg.x = 4000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C4():
    msg.x = 5000
    msg.y = 3000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D1():
    msg.x = 2000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D2():
    msg.x = 3000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D3():
    msg.x = 4000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D4():
    msg.x = 5000
    msg.y = 4000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E1():
    msg.x = 2000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E2():
    msg.x = 3000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E3():
    msg.x = 4000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E4():
    msg.x = 5000
    msg.y = 5000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)

if __name__=='__main__':
    try:
        start()
    except rospu.ROSInterruptException:
        pass
