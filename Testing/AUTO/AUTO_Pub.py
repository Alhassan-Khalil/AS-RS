from time import sleep
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
import rospy
import RPi.GPIO as GPIO
import MFRC522
import Msg_Publisher_place
import numpy as np
import signal


continue_reading = True


def main():
        global root
    	root = Tk()
    	root.title('Main')
    	root.configure(background="Red")
    	Name = Label(root,bg="#999999",fg ="#cc0000",text = "LegenTronics", font = ('Comic Sans MS',30),)
    	Name.pack(side=TOP)
    	frame = LabelFrame(root,padx=50 , pady=50)
    	frame.pack(padx=50)
        def exit():
            root.destroy()
        b2 = Button(frame,text ="EXIT",width=20 ,height=5 ,command=exit)
        b2.grid(row=0,column=1)
        b = Button(frame,text = "Reset" , width = 20 , height = 5 , command=Auto)
        b.grid(row=0,column=0)
    	root.mainloop()




# Capture SIGINT for cleanup when the script is aborted
def exit(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, exit)

MIFAREReader = MFRC522.MFRC522()

def Auto():
    while continue_reading:
        if status == MIFAREReader.MI_OK:
            print("Card detected")
            Msg_Publisher_place.Orgin
            sleep(2)
            placing(0,0,0)


def placing(i,j,k):
    file = open("Storge", "rb")
    ST= np.load(file)
    if i == 7 and j == 3:
        print("The Stoege is Full")
    elif ST[i,j] == 0:
        ST[i,j] = 1
        Msg_Publisher_place.Unit[k]()
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
            return(placing(i,j))
        else:
            j += 1
            k += 1
            return(placing(i,j))
