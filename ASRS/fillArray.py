from tkinter import *
import S1


def main():
	global root
	root = Tk()
	# root.attributes('-zoomed', True)
	root.title('Main')
	global new_window
	new_window = root
	# root.geometry("1350x900+0+0")
	root.configure(background="powder blue")
	Name = Label(root,bg="#999999",fg ="#cc0000",text = "LegenTronics", font = ('Comic Sans MS',30),)
	Name.pack(side=TOP)
	frame = LabelFrame(root,padx=50 , pady=50)
	frame.pack(padx=50)

	def Store():
		S1.placing(0,0)
     	
	def Retrieval():
		S1.taking(0,0)
		
	def exit():
		root.destroy()
        	

	b=Button(frame,bg="#1e90ff",text="Storge",width=20,height=5,command=Store)
	b2=Button(frame,text="Retrieval",width=20,height=5,command=Retrieval)
	b3=Button(frame,text="EXIT",bg="#cc0000",width=20,height=5,command=exit)
	b.grid(row=0,column=0)
	b2.grid(row=0,column=1)
	b3.grid(row=0,column=2)

	root.mainloop()



if __name__ == "__main__":
	main()
