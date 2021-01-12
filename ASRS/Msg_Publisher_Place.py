import rospy
from geometry_msgs.msg import Point
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
    global home
    global ST
    global stop
    rospy.init_node("motor", anonymous=True)
    pub = rospy.Publisher('motor',Point, queue_size=10)
    place = rospy.Publisher('place',Empty,queue_size=10)
    take = rospy.Publisher('take',Empty,queue_size=10)
    home = rospy.Publisher('home',Empty,queue_size=10)
    stop = rospy.Publisher('home',Empty,queue_size=10)
    rate = rospy.Rate(1)
    #---------------
    file = open("Storge", "rb")
    ST= np.load(file)


def Orgin():
   # msg.x = 0
   # msg.y = 0
    rospy.loginfo("motor going to Orgin ")
    home.publish()
    
def Stop():
    rospy.loginfo("Stoping")
    stop.publish()

def A1():
    msg.x = 80500
    msg.y = 92000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,0] == 0 :
        take.publish()
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[0,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()

    else:
        # messagebox.showerror("error", "try again")
        # messagebox.showinfo("my message","this is an example of showinfo\nmessagebox")
        messagebox.showwarning("warning", "A1 unit is FULL" )

def A2():
    msg.x = 61000
    msg.y = 92000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,1] == 0 :
        take.publish()
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[0,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "A2 unit is FULL" )


def A3():
    msg.x = 41500
    msg.y = 92000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,2] == 0 :
        take.publish()
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[0,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "A3 unit is FULL" )


def A4():
    msg.x = 22600
    msg.y = 92000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[0,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[0,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "A4 unit is FULL" )
def B1():
    msg.x = 80500
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[1,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "B1 unit is FULL" )


def B2():
    msg.x = 61000
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[1,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "B2 unit is FULL" )

def B3():
    msg.x = 41500
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,2] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[1,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "B3 unit is FULL" )

def B4():
    msg.x = 22600
    msg.y = 80000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[1,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[1,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "B4 unit is FULL" )

def C1():
    msg.x = 80500
    msg.y = 68000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[2,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "C1 unit is FULL" )

def C2():
    msg.x = 61000
    msg.y = 68000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[2,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "C2 unit is FULL" )

def C3():
    msg.x = 41500
    msg.y = 68000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,2] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[2,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "C3 unit is FULL" )

def C4():
    msg.x = 22600
    msg.y = 68000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[2,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[2,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "C4 unit is FULL" )

def D1():
    msg.x = 80500
    msg.y = 56000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[3,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "D1 unit is FULL" )

def D2():
    msg.x = 61000
    msg.y = 56000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[3,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "D2 unit is FULL" )

def D3():
    msg.x = 41500
    msg.y = 56000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,2] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[3,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "D3 unit is FULL" )

def D4():
    msg.x = 22600
    msg.y = 56000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[3,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[3,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(15.)
        Orgin()
    else:
        messagebox.showwarning("warning", "D1 unit is FULL" )

def E1():
    msg.x = 80500
    msg.y = 44000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[4,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "E1 unit is FULL" )

def E2():
    msg.x = 61000
    msg.y = 44000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[4,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "E2 unit is FULL" )

def E3():
    msg.x = 41500
    msg.y = 44000
    file = open46000("Storge", "rb")
    ST= np.load(file)
    if ST[4,2] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[4,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "E3 unit is FULL" )

def E4():
    msg.x = 22600
    msg.y = 44000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[4,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[4,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "E4 unit is FULL" )


def F1():
    msg.x = 80500
    msg.y = 32000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[5,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "F1 unit is FULL" )

def F2():
    msg.x = 61000
    msg.y = 32000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[5,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "F2 unit is FULL" )

def F3():
    msg.x = 41500
    msg.y = 32000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,2] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[5,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "F3 unit is FULL" )

def F4():
    msg.x = 22600
    msg.y = 32000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[5,3] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[5,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "F1 unit is FULL" )

def G1():
    msg.x = 80500
    msg.y = 20500
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,0] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[6,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "G1 unit is FULL" )

def G2():
    msg.x = 61000
    msg.y = 20500
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,1] == 0 :
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[6,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "G2 unit is FULL" )

def G3():
    msg.x = 41500
    msg.y = 20500
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,2] == 0 :
        rospy.sleep(5.)
        take.publish()
        rospy.loginfo("motor taking")
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(15.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[6,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "G3 unit is FULL" )

def G4():
    msg.x = 22600#22000
    msg.y = 20500
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[6,3] == 0 :
        rospy.sleep(5.)
        take.publish()
        rospy.loginfo("motor taking")
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(15.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[6,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "G4 unit is FULL" )

def H1():
    msg.x = 80500
    msg.y = 8000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,0] == 0 :
        rospy.sleep(5.)
        take.publish()
        rospy.loginfo("motor taking")
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(15.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[7,0] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "H1 unit is FULL" )

def H2():
    msg.x = 61000
    msg.y = 8000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,1] == 0 :
        rospy.sleep(5.)
        take.publish()
        rospy.loginfo("motor taking")
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(15.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[7,1] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "H2 unit is FULL" )

def H3():
    msg.x = 41500
    msg.y = 8000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,2] == 0 :
        rospy.sleep(5.)
        take.publish()
        rospy.loginfo("motor taking")
        rospy.sleep(10.)
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(15.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[7,2] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(10.)
        Orgin()
    else:
        messagebox.showwarning("warning", "H3 unit is FULL" )

def H4():
    msg.x = 22600
    msg.y = 8000
    file = open("Storge", "rb")
    ST= np.load(file)
    if ST[7,3] == 0 :
        rospy.sleep(5.)
        take.publish()
        pub.publish(msg)
        rospy.loginfo("motor going to :x=%d y=%d" %(msg.x,msg.y))
        rospy.sleep(10.)
        place.publish()
        rospy.loginfo("motor placing")
        ST[7,3] = 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        rospy.sleep(15.)
        Orgin()
    else:
        messagebox.showwarning("warning", "H4 unit is FULL" )


Unit = [A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4,E1,E2,E3,E4,F1,F2,F3,F4,G1,G2,G3,G4,H1,H2,H3,H4]



if __name__=='__main__':
    try:
        start()
    except rospu.ROSInterruptException:
        pass
