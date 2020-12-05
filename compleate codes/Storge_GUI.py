from tkinter import *
import main_GUI
import Msg_Publisher
# import Subsicriberpublisher
import rospy
from geometry_msgs.msg import Point, Twist




def Storge():

	global st_root
	st_root = Tk()
	st_root.attributes('-zoomed', True)
	st_root.title('Storage')
	# st_root.geometry("1350x900+0+0")
	st_root.configure(background="powder blue")






	Name = Label(st_root,bg="#999999",fg ="#cc0000",text = "Storage", font = ('Comic Sans MS',30),)
	Name.pack(side=TOP)
	frame = LabelFrame(st_root,padx=50 , pady=50)
	frame.pack(side=RIGHT)
	frame2 = LabelFrame(st_root,padx=50 , pady=50)
	frame2.pack(side=LEFT)


	b=Button(frame,text="A1",width=20,height=10,command=Msg_Publisher.A1)
	b.grid(row=0,column=0)
	b2=Button(frame,text="A2",width=20,height=10,command=Msg_Publisher.A2)
	b2.grid(row=0,column=1)
	b3=Button(frame,text="A3",width=20,height=10,command=Msg_Publisher.A3)
	b3.grid(row=0,column=2)
	b4=Button(frame,text="A4",width=20,height=10,command=Msg_Publisher.A4)
	b4.grid(row=0,column=3)
	b5=Button(frame,text="B1",width=20,height=10,command=Msg_Publisher.B1)
	b5.grid(row=1,column=0)
	b6=Button(frame,text="B2",width=20,height=10,command=Msg_Publisher.B2)
	b6.grid(row=1,column=1)
	b7=Button(frame,text="B3",width=20,height=10,command=Msg_Publisher.B3)
	b7.grid(row=1,column=2)
	b8=Button(frame,text="B4",width=20,height=10,command=Msg_Publisher.B4)
	b8.grid(row=1,column=3)
	b9=Button(frame,text="C1",width=20,height=10,command=Msg_Publisher.C1)
	b9.grid(row=2,column=0)
	b10=Button(frame,text="C2",width=20,height=10,command=Msg_Publisher.C2)
	b10.grid(row=2,column=1)
	b11=Button(frame,text="C3",width=20,height=10,command=Msg_Publisher.C3)
	b11.grid(row=2,column=2)
	b12=Button(frame,text="C4",width=20,height=10,command=Msg_Publisher.C4)
	b12.grid(row=2,column=3)
	b13=Button(frame,text="D1",width=20,height=10,command=Msg_Publisher.D1)
	b13.grid(row=3,column=0)
	b14=Button(frame,text="D2",width=20,height=10,command=Msg_Publisher.D2)
	b14.grid(row=3,column=1)
	b15=Button(frame,text="D3",width=20,height=10,command=Msg_Publisher.D3)
	b15.grid(row=3,column=2)
	b16=Button(frame,text="D4",width=20,height=10,command=Msg_Publisher.D4)
	b16.grid(row=3,column=3)
	b17=Button(frame,text="E1",width=20,height=10,command=Msg_Publisher.E1)
	b17.grid(row=4,column=0)
	b18=Button(frame,text="E2",width=20,height=10,command=Msg_Publisher.E2)
	b18.grid(row=4,column=1)
	b19=Button(frame,text="E3",width=20,height=10,command=Msg_Publisher.E3)
	b19.grid(row=4,column=2)
	b20=Button(frame,text="E4",width=20,height=10,command=Msg_Publisher.E4)
	b20.grid(row=4,column=3)


	b21=Button(frame2,text="AUTO",bg="#5fb878",width=20,height=3)
	b21.grid(row=1,column=0)
	b22=Button(frame2,text="STOP",bg="#cc0000",width=20,height=3)
	b22.grid(row=2,column=0)
	b23=Button(frame2,text="BACK",width=20,height=3 ,command=back)
	b23.grid(row=3,column=0)

	Msg_Publisher.start()
	st_root.mainloop()

def back():
	st_root.destroy()
	main_GUI.main()


if __name__ == "__main__":
	Storge()
