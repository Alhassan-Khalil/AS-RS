from tkinter import *
import time as tm
from datetime import date
import os
import time
from subprocess import call,Popen

Today = date.today()


def main():

	root = Tk()
	root.title('Main')
	root.geometry("1350x900+0+0")
	root.configure(background="powder blue")

	def START():
		# X_value = int(Motoe1_Entry.get())
		# Y_value = int(Motoe2_Entry.get())
		# Popen(['xterm', '-e', 'rostopic pub /motor1/start geometry_msgs/Point "x: %d y: 0.0 z: 0.0"'])
		print("command")
		print(int(Motoe1_Entry.get()))


	Motor1 = Label(root, text= "Motor x ")
	Motor1.place(x=10,y=110,width=201,height=45)
	Motor2 = Label(root, text= "Motor x ")
	Motor2.place(x=10,y=50,width=201,height=46)
	#Motoe1_Entry = Entry(root,textvariable=X_value, width=30)
	Motoe1_Entry = Entry(root,width=30)
	Motoe1_Entry.place(x=220,y=50,width=79,height=48)
	Motoe2_Entry = Entry(root,width=30)
	Motoe2_Entry.place(x=220,y=110,width=81,height=43)

	Start = Button(root, text="START", command=START)
	Start.place(x=320,y=90,width=104,height=30)

	root.mainloop()
if __name__ == "__main__":
	main()
	# root = Tk()
    # root.mainloop()
