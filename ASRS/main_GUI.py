from tkinter import *
import numpy as np
import pandas as pd
import os.path
import PIL
from PIL import ImageTk
from PIL import Image
import time as tm
from datetime import date
import Storge_GUI
import Retrieval_GUI


Today = date.today()


def main():
	global root
	root = Tk()
	img1 = Image.open('LegenTronics_logo.png')
	reimg = img1.resize((250,225),Image.ANTIALIAS)
	img = ImageTk.PhotoImage(reimg)
	# Setting icon of master window
	root.iconphoto(False, img)
	#root.attributes('-zoomed', True)
	
	root.title('AS/RS')
	global new_window
	new_window = root
	root.geometry("1280x720+0+0")
	root.configure(background="SlateGray3")
	Name = Label(root,bg="SlateGray3",fg ="#cc0000",text = "LegenTronics", font = ('Comic Sans MS',40),)
	Name.pack(side=TOP)
	logo = Label(root,image = img,padx=10,pady=10,bg="SlateGray3")
	logo.pack(side=TOP) 
	
	frame = LabelFrame(root,padx=50 , pady=50,bg="SlateGray4")
	frame.pack(padx=50 )


	def GoStorage():
		root.destroy()
		Storge_GUI.Storge()

	def GoRetrieval():
		root.destroy()
		Retrieval_GUI.Retrieval()

	def exit_main():
		root.destroy()

	b=Button(frame,bg="#1e90ff",text="Storge",width=20,height=5,command=GoStorage)
	b2=Button(frame,text="Retrieval",width=20,height=5,command=GoRetrieval)
	b3=Button(frame,text="EXIT",bg="#cc0000",width=20,height=5,command=exit_main)
	b.grid(row=0,column=0)
	b2.grid(row=0,column=1)
	b3.grid(row=0,column=2)

	root.mainloop()

if __name__ == "__main__":
    if os.path.isfile('Storge'):
        print ("File exist")
        file = open("Storge", "rb")
        #read the file to numpy array
        ST= np.load(file)
        #close the file
        print("loading the array")
        main()
    else:
        print ("File not exist")
        ST= np.zeros((8, 4), int)
        file = open("Storge", "wb")
        np.save(file, ST)
        file.close
        df = pd.DataFrame (ST)
        filepath = 'my_excel_file.xlsx'
        df.to_excel(filepath, index=False)
        main()
