import rospy
from geometry_msgs.msg import Point, Twist

# global msg

def start():
    global msg
    pub = rospy.Publisher('motor',Point, queue_size=10)
    rospy.init_node("motor", anonymous=True)
    # while not rospy.is_shutdown():
    msg= Point()
    msg.x = 1000
    msg.y = 1500
    rospy.loginfo("motor postion:x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)

# if __name__=='__main__':
#     start()
