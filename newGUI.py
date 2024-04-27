import tkinter as tk
import methods as methods
import speech_to_text as sr
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("VoicePilot")
app.geometry("400x190")

# available_microphones = methods.get_available_microphones()
available_microphones = ["none", "test11", "test12"]
mic_name = available_microphones[0]
mic_index = 0

# available_cameras = methods.get_available_cameras()
available_cameras = ["none", "test21", "test22"]
camera_name = available_cameras[0]
camera_index = 0

def leaveApp():
    app.destroy()
    exit()
    
def exitApp(event):
    app.destroy()
    exit()
    
def faceToggleEvent():
    print(faceSwitchVar.get())
    # if faceSwitchVar.get() == "on":
    #     #
    # else
    #     #

def speechToggleEvent():
    print(speechSwitchVar.get())
    # if speechSwitchVar.get() == "on":
    #     #
    # else
    #     #
    
def cameraOptions(choice):
    print(choice)

def audioOptions(choice):
    print(choice)

app.grid_columnconfigure(0, weight = 1)
app.grid_columnconfigure(1, weight = 1)
app.grid_columnconfigure(2, weight = 1)

quitButton = ctk.CTkButton(app, text = "Quit", command = leaveApp)

titleLabel = ctk.CTkLabel(app, text = "VoicePilot", font = ("Helvetica", 30))
toggleLabel = ctk.CTkLabel(app, text = "Toggles", font = ("Helvetica", 20))
settingsLabel = ctk.CTkLabel(app, text = "Settings", font = ("Helvetica", 20))

faceSwitchVar = ctk.StringVar(value = "off")
faceSwitch = ctk.CTkSwitch(app, text = "Facial Recognition", command=faceToggleEvent, variable=faceSwitchVar, onvalue="on", offvalue="off")

speechSwitchVar = ctk.StringVar(value = "off")
speechSwitch = ctk.CTkSwitch(app, text = "Speech Recognition", command=speechToggleEvent, variable=speechSwitchVar, onvalue="on", offvalue="off")

cameraMenuVar = ctk.StringVar(value = available_cameras[0])
cameraMenu = ctk.CTkOptionMenu(app, values = available_cameras, command=cameraOptions, variable=cameraMenuVar)

audioMenuVar = ctk.StringVar(value = available_microphones[0])
audioMenu = ctk.CTkOptionMenu(app, values = available_microphones, command=audioOptions, variable=audioMenuVar)

titleLabel.grid(row = 0, column = 0, padx = 20, pady = (5,2), columnspan = 4)
toggleLabel.grid(row = 1, column = 0, padx = 10, pady = 2, columnspan = 1)
settingsLabel.grid(row = 1, column = 1, padx = 10, pady = 2, columnspan = 1)
faceSwitch.grid(row = 2, column = 0, sticky="w", padx=10, pady=2)
speechSwitch.grid(row = 3, column = 0, sticky="w", padx=10, pady=2)

cameraMenu.grid(row = 2, column = 1, padx=10, pady=2)
audioMenu.grid(row = 3, column = 1, padx=10, pady=2)

quitButton.grid(row=4, column=0, columnspan=4,pady=10,padx=10)

app.bind('<Escape>', exitApp) #FAILSAFE DO NOT DELETE PLS
app.mainloop()

