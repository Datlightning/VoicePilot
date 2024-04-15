import tkinter as tk
import methods as methods
import speech_to_text as sr


speechActive = False
faceActive = False

def final():
    def speechRec():
        global speechActive 
        speechActive = not speechActive
        if speechActive:
            b1.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            b1.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
        speechToggle()
    def faceRec():
        global faceActive
        faceActive = not faceActive
        if faceActive:
            b2.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            b2.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
        faceToggle()
    def exit_app():
        window.destroy()
        exit()
    methods.setup()
    window = tk.Tk()
    window.title("HELPER")
    window.resizable(width=True, height=True)
    window.geometry("450x220")
    
    title = tk.Label(window, text = "VoicePilot", font= ('Helvetica 25 bold'))
    
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    
    # image = Image.open('logo.png')
    # image = ImageTk.PhotoImage(image)
    # image_label = tk.Label(window, image=image)
    
    l1 = tk.Label(window, text = "Toggle Speech Recognition", font= ('Helvetica 15'))
    l2 = tk.Label(window, text = "Toggle Facial Recognition", font= ('Helvetica 15'))
    
    b1 = tk.Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=speechRec, bg = "red", fg = "white", bd = 4, width = 12)
    b2 = tk.Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=faceRec, bg = "red", fg = "white", bd = 4, width = 12)
    
    b3 = tk.Button(window, text = "Quit", font= ('Helvetica 15'), command=exit_app, bd = 4)
    
    title.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)
    
    l1.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 5)
    l2.grid(row = 3, column = 0, sticky = tk.W, padx = 10, pady = 5)
    
    b1.grid(row = 2, column = 1, sticky = tk.E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    b2.grid(row = 3, column = 1, sticky = tk.E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    b3.grid(row = 4, column = 0, padx = 10, pady = 5, rowspan = 2, columnspan = 2)
    window.iconbitmap('logo.ico')



    while True:                                                                                                                                                 
        if speechActive:
            data = sr.getData()
            if isinstance(data, int):
                print(data)
                pass
            elif data:
                print(data)
                instructions = methods.get_instructions(data)
                print(instructions)
                
                extra = methods.handleinstructions(instructions)
                if extra == "face_track":
                    faceRec()
        window.update_idletasks()
        window.update()

def speechToggle():
    # put your code here shreyas
    if speechActive:
        sr.start()
    else:
        sr.end()
    
    
def faceToggle():
    if faceActive:
        methods.startFaceTrack()
    else:
        methods.pauseFaceTrack()


def main():
    final()

if __name__ == '__main__':
    main()