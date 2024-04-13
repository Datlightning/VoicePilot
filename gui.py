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
            b1.configure(bg="#00FF00", text=" ACTIVE ")
            window.update()
        else:
            b1.configure(bg = "red", text="INACTIVE")
            window.update()
    def faceRec():
        faceToggle()
        global faceActive
        faceActive = not faceActive
        if faceActive:
            b2.configure(bg="#00FF00", text=" ACTIVE ")
            window.update()
        else:
            b2.configure(bg = "red", text="INACTIVE")
            window.update()
    window = tk.Tk()
    window.title("HELPER")
    window.resizable(width=True, height=True)
    window.geometry("450x200")
    
    title = Label(window, text = "HELPER", font= ('Courier 25'))
    
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    
    l1 = Label(window, text = "Toggle Speech Recognition", font= ('Courier 15'))
    l2 = Label(window, text = "Toggle Facial Recognition", font= ('Courier 15'))
    
    b1 = Button(window, text = "INACTIVE", font= ('Courier 15 bold'), command=speechRec, bg = "red")
    b2 = Button(window, text = "INACTIVE", font= ('Courier 15 bold'), command=faceRec, bg = "red")
    
    if (speechActive):
        b1["bg"] = "green"
        b1["text"] = "ACTIVE"
        print("speech is active")
    if (faceActive):
        b2["bg"] = "green"
        b2["text"] = "ACTIVE"
        print("face is active")
    
    b3 = Button(window, text = "Quit", font= ('Courier 15'), command=window.destroy)
    
    title.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)
    
    l1.grid(row = 2, column = 0, sticky = W, padx = 10, pady = 5)
    l2.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 5)
    
    b1.grid(row = 2, column = 1, sticky = E, padx = 10, pady = 5)
    b2.grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
    b3.grid(row = 4, column = 0, padx = 10, pady = 5, rowspan = 2, columnspan = 2)
    
    window.bind('<Escape>', lambda e: window.destroy())
    window.mainloop()

def speechToggle():
    print("speech is toggling")
    
def faceToggle():
    print("face is toggling")


def main():
    final()

if __name__ == '__main__':
    main()