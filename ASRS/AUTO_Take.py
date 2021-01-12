from tkinter import *
from time import sleep
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
import rospy
import RPi.GPIO as GPIO
import MFRC522
import Msg_Publisher_take
import numpy as np
import signal
import pandas as pd


after_id = None
secs = 0
def main():
    global root
    root = Tk()
    root.title('Main')
    root.configure(background="Red")
    Name = Label(root,bg="#999999",fg ="#cc0000",text = "LegenTronics", font = ('Comic Sans MS',30),)
    Name.pack(side=TOP)
    frame = LabelFrame(root,padx=50 , pady=50)
    frame.pack(padx=50)
    def exit1():
    	root.destroy()
    b2 = Button(frame,text ="/",width=20 ,height=5 ,command=exit)
    b2.grid(row=0,column=1)
    b = Button(frame,text = "Auto" , width = 20 , height = 5 , command=start)
    b.grid(row=0,column=0)
    b3 = Button(frame,text = "EXIT" , width = 20 , height = 5 , command=exit)
    b3.grid(row=0,column=2)
    root.mainloop()




# Capture SIGINT for cleanup when the script is aborted
def exit():
    global after_id
    if after_id:
    	root.after_cancel(after_id)
    	after_id = None
    	GPIO.cleanup()
    	root.destroy()

# Hook the SIGINT
signal.signal(signal.SIGINT, exit)

MIFAREReader = MFRC522.MFRC522()



def start():
    global secs
    secs = 0
    Auto()  # start repeated checking

def Auto():
    Msg_Publisher_take.start()
    global root
    global secs
    global after_id
    secs += 1
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    if status == MIFAREReader.MI_OK:
    	print("Card detected")
    	Msg_Publisher_take.Orgin
    	taking(0,0,0)
    after_id = root.after(1000, Auto)  # check again in 1


def taking(i,j,k):
    file = open("Storge", "rb")
    ST= np.load(file)
    if i == 7 and j == 3:
        print("The Stoege is Full")
    elif ST[i,j] == 1:
        ST[i,j] = 0
        Msg_Publisher_take.Unit[k]()
        ##k+= 1
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        df = pd.DataFrame (ST)
        filepath = 'my_excel_file.xlsx'
        df.to_excel(filepath, index=False)
        print(ST)

        print("------------------------------")
    else:
        print("The place is Full")
        if j == 3 :
            print("The column is Full")
            i += 1
            j = 0
            k+= 1
            return(taking(i,j,k))
        else:
            j += 1
            k += 1
            return(taking(i,j,k))
            
            
            
if __name__ == "__main__":
	main()
