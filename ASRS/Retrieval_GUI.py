from tkinter import *
import main_GUI
import Msg_Publisher_take
import AUTO_Take
import os.path
import PIL
from PIL import ImageTk
from PIL import Image
import numpy as np



def Retrieval():

	global re_root
	re_root = Tk()
	re_root.attributes('-zoomed', True)
	re_root.title('Retrieval')
	img1 = Image.open('LegenTronics_logo.png')
	reimg = img1.resize((250,225),Image.ANTIALIAS)
	img = ImageTk.PhotoImage(reimg)
	# Setting icon of master window
	re_root.iconphoto(False, img)
	# re_root.geometry("1350x900+0+0")
	re_root.configure(background="SlateGray3")

	Name = Label(re_root,bg="SlateGray3",fg ="#cc0000",text = "Retrieval", font = ('Ubuntu',30),)
	Name.pack(side=TOP)
	frame = LabelFrame(re_root,bg="SlateGray4",padx=50 , pady=50)
	frame.pack(side=RIGHT)
	frame2 = LabelFrame(re_root,bg="SlateGray4",padx=50 , pady=50)
	frame2.pack(side=LEFT)


	b=Button(frame,text="A1",width=15,height=2,command=Msg_Publisher_take.A1)
	b.grid(row=0,column=0)
	b2=Button(frame,text="A2",width=15,height=2,command=Msg_Publisher_take.A2)
	b2.grid(row=0,column=1)
	b3=Button(frame,text="A3",width=15,height=2,command=Msg_Publisher_take.A3)
	b3.grid(row=0,column=2)
	b4=Button(frame,text="A4",width=15,height=2,command=Msg_Publisher_take.A4)
	b4.grid(row=0,column=3)
	b5=Button(frame,text="B1",width=15,height=2,command=Msg_Publisher_take.B1)
	b5.grid(row=1,column=0)
	b6=Button(frame,text="B2",width=15,height=2,command=Msg_Publisher_take.B2)
	b6.grid(row=1,column=1)
	b7=Button(frame,text="B3",width=15,height=2,command=Msg_Publisher_take.B3)
	b7.grid(row=1,column=2)
	b8=Button(frame,text="B4",width=15,height=2,command=Msg_Publisher_take.B4)
	b8.grid(row=1,column=3)
	b9=Button(frame,text="C1",width=15,height=2,command=Msg_Publisher_take.C1)
	b9.grid(row=2,column=0)
	b10=Button(frame,text="C2",width=15,height=2,command=Msg_Publisher_take.C2)
	b10.grid(row=2,column=1)
	b11=Button(frame,text="C3",width=15,height=2,command=Msg_Publisher_take.C3)
	b11.grid(row=2,column=2)
	b12=Button(frame,text="C4",width=15,height=2,command=Msg_Publisher_take.C4)
	b12.grid(row=2,column=3)
	b13=Button(frame,text="D1",width=15,height=2,command=Msg_Publisher_take.D1)
	b13.grid(row=3,column=0)
	b14=Button(frame,text="D2",width=15,height=2,command=Msg_Publisher_take.D2)
	b14.grid(row=3,column=1)
	b15=Button(frame,text="D3",width=15,height=2,command=Msg_Publisher_take.D3)
	b15.grid(row=3,column=2)
	b16=Button(frame,text="D4",width=15,height=2,command=Msg_Publisher_take.D4)
	b16.grid(row=3,column=3)
	b17=Button(frame,text="E1",width=15,height=2,command=Msg_Publisher_take.E1)
	b17.grid(row=4,column=0)
	b18=Button(frame,text="E2",width=15,height=2,command=Msg_Publisher_take.E2)
	b18.grid(row=4,column=1)
	b19=Button(frame,text="E3",width=15,height=2,command=Msg_Publisher_take.E3)
	b19.grid(row=4,column=2)
	b20=Button(frame,text="E4",width=15,height=2,command=Msg_Publisher_take.E4)
	b20.grid(row=4,column=3)
	b21=Button(frame,text="F1",width=15,height=2,command=Msg_Publisher_take.F1)
	b21.grid(row=5,column=0)
	b22=Button(frame,text="F2",width=15,height=2,command=Msg_Publisher_take.F2)
	b22.grid(row=5,column=1)
	b23=Button(frame,text="F3",width=15,height=2,command=Msg_Publisher_take.F3)
	b23.grid(row=5,column=2)
	b24=Button(frame,text="F4",width=15,height=2,command=Msg_Publisher_take.F4)
	b24.grid(row=5,column=3)
	b25=Button(frame,text="G1",width=15,height=2,command=Msg_Publisher_take.G1)
	b25.grid(row=6,column=0)
	b26=Button(frame,text="G2",width=15,height=2,command=Msg_Publisher_take.G2)
	b26.grid(row=6,column=1)
	b27=Button(frame,text="G3",width=15,height=2,command=Msg_Publisher_take.G3)
	b27.grid(row=6,column=2)
	b28=Button(frame,text="G4",width=15,height=2,command=Msg_Publisher_take.G4)
	b28.grid(row=6,column=3)
	b29=Button(frame,text="H1",width=15,height=2,command=Msg_Publisher_take.H1)
	b29.grid(row=7,column=0)
	b30=Button(frame,text="H2",width=15,height=2,command=Msg_Publisher_take.H2)
	b30.grid(row=7,column=1)
	b31=Button(frame,text="H3",width=15,height=2,command=Msg_Publisher_take.H3)
	b31.grid(row=7,column=2)
	b32=Button(frame,text="H4",width=15,height=2,command=Msg_Publisher_take.H4)
	b32.grid(row=7,column=3)



	b33=Button(frame2,text="AUTO",bg="#5fb878",width=20,height=3, command=AUTO_Take.main)
	b33.grid(row=0,column=0)
	label1=Label(frame2,bg="SlateGray4",text = "Automatic Retrieval")
	label1.grid(row=0,column=1)
	
	b34 = Button(frame2,text = "Reset" , width = 20 , height = 3 , command=Reset)
	b34.grid(row=2,column=0)
	label2=Label(frame2,bg="SlateGray4",text = "Reset all units")
	label2.grid(row=2,column=1)
	
	b35=Button(frame2,text="STOP",bg="#cc0000",width=20,height=3, command=AUTO_Take.exit)
	b35.grid(row=1,column=0)
	b36=Button(frame2,text="BACK",width=20,height=3 ,command=back)
	b36.grid(row=4,column=0)
	b37=Button(frame2,text="Orgin",width=20,height=3 ,command=Msg_Publisher_take.Orgin)
	b37.grid(row=3,column=0)
	label3=Label(frame2,bg="SlateGray4",text = "Going to the home position ")
	label3.grid(row=3,column=1)

	Msg_Publisher_take.start()
	re_root.mainloop()


def back():
	re_root.destroy()
	main_GUI.main()

def Reset():
	if os.path.isfile('Storge'):
		file = open("Storge", "rb")
		ST= np.load(file)
		for i in range(0,8):
			for j in range(0,4):
				if ST[i,j] == 1:
					ST[i,j] = 0
					print(ST)
					file = open("Storge", "wb")
					np.save(file, ST)
	else:
		ST= np.zeros((8, 4), int)
		file = open("Storge", "wb")
		np.save(file, ST)
		file.close


if __name__ == "__main__":
	Retrieval()
