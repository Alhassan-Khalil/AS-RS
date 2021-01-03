import rospy
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
from time import sleep
from tkinter import messagebox
import numpy as np



global msg
msg= Point()

def start():
    global pub
    global place
    global take
    global ST
    rospy.init_node("motor", anonymous=True)
    pub = rospy.Publisher('motor',Point, queue_size=10)
    place = rospy.Publisher('place',Empty,queue_size=10)
    take = rospy.Publisher('take',Empty,queue_size=10)
    rate = rospy.Rate(1)
    #---------------

    file = open("Storge", "rb")
    ST= np.load(file)


def Orgin():
    msg.x = 100
    msg.y = 100
    rospy.loginfo("motor going to Orgin :x=%d y=%d" %(msg.x,msg.y))
    pub.publish(msg)


def A1():
    msg.x = 10000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[0,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "A1 unit is Empty" )

def A2():
    msg.x = 10000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[0,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "A2 unit is Empty" )


def A3():
    msg.x = 50000
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[0,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "A3 unit is Empty" )


def A4():
    msg.x = 70000
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[0,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "A4 unit is Empty" )
def B1():
    msg.x = 10000
    msg.y = 70000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[1,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "B1 unit is Empty" )


def B2():
    msg.x = 30000
    msg.y = 70000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[1,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "B2 unit is Empty" )

def B3():
    msg.x = 50000
    msg.y = 70000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[1,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "B3 unit is Empty" )

def B4():
    msg.x = 70000
    msg.y = 70000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[1,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "B4 unit is Empty" )

def C1():
    msg.x = 10000
    msg.y = 60000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[2,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "C1 unit is Empty" )

def C2():
    msg.x = 30000
    msg.y = 60000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[2,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "C2 unit is Empty" )

def C3():
    msg.x = 50000
    msg.y = 60000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[2,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "C3 unit is Empty" )

def C4():
    msg.x = 70000
    msg.y = 60000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[2,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "C4 unit is Empty" )

def D1():
    msg.x = 10000
    msg.y = 50000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[3,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "D1 unit is Empty" )

def D2():
    msg.x = 30000
    msg.y = 50000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[3,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "D2 unit is Empty" )

def D3():
    msg.x = 50000
    msg.y = 50000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[3,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "D3 unit is Empty" )

def D4():
    msg.x = 70000
    msg.y = 50000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[3,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "D1 unit is Empty" )

def E1():
    msg.x = 10000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[4,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "E1 unit is Empty" )

def E2():
    msg.x = 30000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[4,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "E2 unit is Empty" )

def E3():
    msg.x = 50000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[4,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "E3 unit is Empty" )

def E4():
    msg.x = 70000
    msg.y = 40000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[4,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "E4 unit is Empty" )


def F1():
    msg.x = 10000
    msg.y = 30000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[5,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "F1 unit is Empty" )

def F2():
    msg.x = 30000
    msg.y = 30000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[5,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "F2 unit is Empty" )

def F3():
    msg.x = 50000
    msg.y = 30000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[5,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "F3 unit is Empty" )

def F4():
    msg.x = 70000
    msg.y = 30000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[5,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "F1 unit is Empty" )

def G1():
    msg.x = 10000
    msg.y = 20000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[6,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "G1 unit is Empty" )

def G2():
    msg.x = 30000
    msg.y = 20000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[6,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "G2 unit is Empty" )

def G3():
    msg.x = 50000
    msg.y = 20000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[6,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "G3 unit is Empty" )

def G4():
    msg.x = 70000
    msg.y = 20000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[6,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "G4 unit is Empty" )

def H1():
    msg.x = 10000
    msg.y = 10000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,0] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[7,0] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "H1 unit is Empty" )

def H2():
    msg.x = 30000
    msg.y = 10000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,1] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[7,1] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "H2 unit is Empty" )

def H3():
    msg.x = 50000
    msg.y = 10000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,2] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[7,2] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "H3 unit is Empty" )

def H4():
    msg.x = 70000
    msg.y = 10000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,3] == 1 :
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        sleep(5)
        take.publish()
        rospy.loginfo("motor placing")
        sleep(5)
        Orgin()
        sleep(5)
        place.publish()
        ST[7,3] = 0
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
    else:
        messagebox.showwarning("warning", "H4 unit is Empty" )


if __name__=='__main__':
    try:
        start()
    except rospu.ROSInterruptException:
        pass
