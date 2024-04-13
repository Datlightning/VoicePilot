import tkinter as tk
from tkinter import *

def testGrid():
    window = tk.Tk()
    window.title("[INSERT NAME]")
    window.resizable(width=True, height=True)
    #Set the geometry of tkinter frame
    window.geometry("250x750")
    
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=4
            )
            frame.grid(row=i, column=j)
            if (i == 0 and j == 1):
                label1= Label(master=frame, text="Hello There!", font= ('Courier 20 underline'))
                label1.pack()
            else:
                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack(padx = 5, pady = 5)
    
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    window.bind('<Escape>', lambda e: window.destroy())
    # window.iconify() minimize window
    window.mainloop()

speechActive = False
faceActive = False

def final():
    def speechRec():
        speechToggle()
        global speechActive 
        speechActive = not speechActive
        if speechActive:
            b1.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            b1.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
    def faceRec():
        faceToggle()
        global faceActive
        faceActive = not faceActive
        if faceActive:
            b2.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            b2.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
    window = tk.Tk()
    window.title("HELPER")
    window.resizable(width=True, height=True)
    window.geometry("450x220")
    
    title = Label(window, text = "HELPER", font= ('Helvetica 25 bold'))
    
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    
    l1 = Label(window, text = "Toggle Speech Recognition", font= ('Helvetica 15'))
    l2 = Label(window, text = "Toggle Facial Recognition", font= ('Helvetica 15'))
    
    b1 = Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=speechRec, bg = "red", fg = "white", bd = 4, width = 12)
    b2 = Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=faceRec, bg = "red", fg = "white", bd = 4, width = 12)
    
    b3 = Button(window, text = "Quit", font= ('Helvetica 15'), command=window.destroy, bd = 4)
    
    title.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)
    
    l1.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)
    l2.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
    
    b1.grid(row = 2, column = 1, sticky = E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    b2.grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    b3.grid(row = 4, column = 0, padx = 10, pady = 5, rowspan = 2, columnspan = 2)
    
    window.bind('<Escape>', lambda e: window.destroy())
    window.mainloop()

def speechToggle():
    # put your code here shreyas
    print("speech is toggling")
    
def faceToggle():
    # put your code here vihas
    print("face is toggling")


def main():
    final()

if __name__ == '__main__':
    main()