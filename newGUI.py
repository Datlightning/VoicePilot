import tkinter as tk
import methods as methods
import speech_to_text as sr
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("VoicePilot")
app.geometry("400x190+400+400")
app.resizable(width=False, height=False)
# app.iconbitmap('logo.ico')

# available_microphones = methods.get_available_microphones()

available_microphones = methods.get_available_microphones()
mic_name = available_microphones[0]
mic_index = 0
def set_microphone(selection):
        """
        Function to set the selected microphone.
        """
        global mic_name
        global mic_index
        mic_name = selection
        mic_index = available_microphones.index(selection)

def leaveApp():
    app.destroy()
    exit()
    
def exitApp(event):
    app.destroy()
    exit()
    
def faceToggleEvent():
    print(faceSwitchVar.get())
    if faceSwitchVar.get() == "on":
        methods.startFaceTrack()
    else:
        methods.pauseFaceTrack()

def speechToggleEvent():
    print(speechSwitchVar.get())
    if speechSwitchVar.get() == "on":
        sr.start(index=mic_index)
    else:
        sr.end()
    
def cameraOptions(choice):
    print(choice)

def audioOptions(choice):
    print(choice)
while True:
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

    def show_dropdown_menu():
            """
            Function to display the dropdown menu.
            """
            # Get a list of available microphones

            # Create a new window for the dropdown menu
            dropdown_window = tk.Toplevel()
            dropdown_window.title("Input Sources")

            # Create a label
            label = tk.Label(dropdown_window, text="Select Microphone:", font= ('Helvetica 15'))
            label.grid(row = 0, column = 0)

            # Create a dropdown menu
            selected_microphone = tk.StringVar(dropdown_window)
            selected_microphone.set(available_microphones[0]) # Set default value
            microphone_menu = tk.OptionMenu(dropdown_window, selected_microphone, *available_microphones, command=set_microphone)
            microphone_menu.grid(row = 0, column = 1)

            # Create a label
            label = tk.Label(dropdown_window, text="Select Camera:", font= ('Helvetica 15'))
            label.grid(row = 1, column = 0)

        



    audioMenu = ctk.CTkOptionMenu(app, values = available_microphones, command=show_dropdown_menu)

    titleLabel.grid(row = 0, column = 0, padx = 20, pady = (5,2), columnspan = 4)
    toggleLabel.grid(row = 1, column = 0, padx = 10, pady = 2, columnspan = 1)
    settingsLabel.grid(row = 1, column = 1, padx = 10, pady = 2, columnspan = 1)
    faceSwitch.grid(row = 2, column = 0, sticky="w", padx=10, pady=2)
    speechSwitch.grid(row = 3, column = 0, sticky="w", padx=10, pady=2)

    audioMenu.grid(row = 3, column = 1, padx=10, pady=2)

    quitButton.grid(row=4, column=0, columnspan=4,pady=10,padx=10)



    app.bind('<Escape>', exitApp) #FAILSAFE DO NOT DELETE PLS
    app.update_idletasks()
    app.update()


