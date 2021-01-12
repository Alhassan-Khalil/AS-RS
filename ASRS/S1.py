from tkinter import *
import numpy as np
import pandas as pd
import os.path



global ST

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
   b = Button(frame,text = "Reset" , width = 20 , height = 5 , command=Reset)
   b.grid(row=0,column=0)
   root.mainloop()





def placing(i,j):
    file = open("Storge", "rb")
    ST= np.load(file)
    if i == 7 and j == 3:
        print("The Stoege is Full")
    elif ST[i,j] == 0:
        ST[i,j] = 1
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
            return(placing(i,j))
        else:
            j += 1
            return(placing(i,j))

def taking(i,j):
    file = open("Storge", "rb")
    ST= np.load(file)
    if i == 7 and j == 3:
        print("The Stoege is Full")
    elif ST[i,j] == 1:
        ST[i,j] = 0
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
            return(taking(i,j))
        else:
            j += 1
            return(taking(i,j))

def Reset():
    for i in range(0,8):
        for j in range(0,4):

            if ST[i,j] == 1:
                ST[i,j] = 0
                print(ST)
                file = open("Storge", "wb")
                np.save(file, ST)

#
# def storge():
#
#     # #create 2D numpy array with zeros
#     # ST = np.zeros((8, 4), int)
#
#     # print("\n")
#     print(ST)
#     # open a binary file in write mode
#     file = open("Storge", "wb")
#     # save array to the file
#     np.save(file, ST)
#     # close the file
#     file.close
#
#     ## convert your array into a dataframe
#     df = pd.DataFrame (S)
#     ## save to xlsx file
#     filepath = 'my_excel_file.xlsx'
#     df.to_excel(filepath, index=False)

#cgeh

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
