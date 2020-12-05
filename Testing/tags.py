import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=469
        height=197
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_443=tk.Label(root)
        GLabel_443["bg"] = "#90f090"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_443["font"] = ft
        GLabel_443["fg"] = "#333333"
        GLabel_443["justify"] = "center"
        GLabel_443["text"] = "Motor x "
        GLabel_443["relief"] = "ridge"
        GLabel_443.place(x=10,y=110,width=201,height=45)

        GLabel_324=tk.Label(root)
        GLabel_324["anchor"] = "n"
        GLabel_324["bg"] = "#90f090"
        GLabel_324["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_324["font"] = ft
        GLabel_324["fg"] = "#393d49"
        GLabel_324["justify"] = "center"
        GLabel_324["text"] = "Motor Y"
        GLabel_324.place(x=10,y=50,width=201,height=46)

        GLineEdit_100=tk.Entry(root)
        GLineEdit_100["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_100["font"] = ft
        GLineEdit_100["fg"] = "#333333"
        GLineEdit_100["justify"] = "center"
        GLineEdit_100["text"] = "0"
        GLineEdit_100.place(x=220,y=50,width=79,height=48)

        GLineEdit_466=tk.Entry(root)
        GLineEdit_466["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_466["font"] = ft
        GLineEdit_466["fg"] = "#333333"
        GLineEdit_466["justify"] = "center"
        GLineEdit_466["text"] = "0"
        GLineEdit_466.place(x=220,y=110,width=81,height=43)

        GButton_18=tk.Button(root)
        GButton_18["bg"] = "#f2f1f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_18["font"] = ft
        GButton_18["fg"] = "#4c4c4c"
        GButton_18["justify"] = "center"
        GButton_18["text"] = "Go"
        GButton_18.place(x=320,y=90,width=104,height=30)
        GButton_18["command"] = self.GButton_18_command

    def GButton_18_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
