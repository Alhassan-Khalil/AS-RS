import rospy
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
from time import sleep

global msg
msg= Point()

def start():
    global pub
    global pub2
    rospy.init_node("motor", anonymous=True)
    pub = rospy.Publisher('motor',Point, queue_size=10)
    pub2 = rospy.Publisher('place',Empty,queue_size=10)


def Orgin():
    msg.x = 0
    msg.y = 0
    rospy.loginfo("motor going to Orgin :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)

def A1():
    msg.x = 10000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    #pub.publish(msg)
    pub2.publish()
def A2():
    msg.x = 10000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    sleep(2)
    pub2.publish()
    rospy.loginfo("motor placing")
def A3():
    msg.x = 50000
    msg.y = 80000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def A4():
    msg.x = 70000
    msg.y = 80000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B1():
    msg.x = 10000
    msg.y = 70000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B2():
    msg.x = 30000
    msg.y = 70000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B3():
    msg.x = 50000
    msg.y = 70000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def B4():
    msg.x = 70000
    msg.y = 70000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C1():
    msg.x = 10000
    msg.y = 60000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub2.publish()
#pub.publish(msg)
def C2():
    msg.x = 30000
    msg.y = 60000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
    pub2.publish()
def C3():
    msg.x = 50000
    msg.y = 60000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def C4():
    msg.x = 70000
    msg.y = 60000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D1():
    msg.x = 10000
    msg.y = 50000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D2():
    msg.x = 30000
    msg.y = 50000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D3():
    msg.x = 50000
    msg.y = 50000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def D4():
    msg.x = 70000
    msg.y = 50000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E1():
    msg.x = 10000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E2():
    msg.x = 30000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E3():
    msg.x = 50000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def E4():
    msg.x = 70000
    msg.y = 40000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)


def F1():
    msg.x = 10000
    msg.y = 30000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def F2():
    msg.x = 30000
    msg.y = 30000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def F3():
    msg.x = 50000
    msg.y = 30000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def F4():
    msg.x = 70000
    msg.y = 30000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def G1():
    msg.x = 10000
    msg.y = 20000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def G2():
    msg.x = 30000
    msg.y = 20000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def G3():
    msg.x = 50000
    msg.y = 20000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def G4():
    msg.x = 70000
    msg.y = 20000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def H1():
    msg.x = 10000
    msg.y = 10000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def H2():
    msg.x = 30000
    msg.y = 10000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def H3():
    msg.x = 50000
    msg.y = 10000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)
def H4():
    msg.x = 70000
    msg.y = 10000
    rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)

if __name__=='__main__':
    try:
        start()
    except rospu.ROSInterruptException:
        pass
