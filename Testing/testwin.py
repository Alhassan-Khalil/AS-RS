import tkinter as tk
root = tk.Tk()
#In order to hide main window
root.withdraw()
tk.Label(root, text="This is the main window").pack()
aWindow = tk.Toplevel(root)
def change_window():
    #remove the other window entirely
    aWindow.destroy()
    #make root visible again
    root.iconify()
    root.deiconify()
tk.Button(aWindow, text="This is aWindow", command=change_window).pack()
root.mainloop()
