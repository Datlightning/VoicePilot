import tkinter as tk
import methods as methods
import speech_to_text as sr

speechActive = False
faceActive = False

available_microphones = methods.get_available_microphones()
mic_name = available_microphones[0]
mic_index = 0

available_cameras = methods.get_available_cameras()
camera_name = available_cameras[0]
camera_index = 0

def final():
    def speechRec():
        global speechActive 
        speechActive = not speechActive
        if speechActive:
            speech_recognition_label.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            speech_recognition_label.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
        speechToggle()
    def faceRec():
        global faceActive
        faceActive = not faceActive
        if faceActive:
            facial_recognition_label.configure(bg="#00FF00", text="ACTIVE", fg="black")
            window.update()
        else:
            facial_recognition_label.configure(bg = "red", text="INACTIVE", fg="white")
            window.update()
        faceToggle()
    def exit_app():
        window.destroy()
        exit()
    methods.setup()
    window = tk.Tk()
    window.title("VoicePilot")
    window.resizable(width=True, height=True)
    window.geometry("450x220")
    
    title = tk.Label(window, text = "VoicePilot", font= ('Helvetica 25 bold'))
    
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    
    # image = Image.open('logo.png')
    # image = ImageTk.PhotoImage(image)
    # image_label = tk.Label(window, image=image)
    
    speech_recognition_label = tk.Label(window, text = "Toggle Speech Recognition", font= ('Helvetica 15'))
    facial_recognition_label = tk.Label(window, text = "Toggle Facial Recognition", font= ('Helvetica 15'))
    
    speech_recongition_button = tk.Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=speechRec, bg = "red", fg = "white", bd = 4, width = 12)
    face_recognition_button = tk.Button(window, text = "INACTIVE", font= ('Helvetica 15 bold'), command=faceRec, bg = "red", fg = "white", bd = 4, width = 12)
    
    quit_button = tk.Button(window, text = "Quit", font= ('Helvetica 15'), command=exit_app, bd = 4)
    
    title.grid(row = 0, column = 0, rowspan = 2, columnspan = 2)
    
    speech_recognition_label.grid(row = 2, column = 0, sticky = tk.W, padx = 10, pady = 5)
    facial_recognition_label.grid(row = 3, column = 0, sticky = tk.W, padx = 10, pady = 5)
    
    speech_recongition_button.grid(row = 2, column = 1, sticky = tk.E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    face_recognition_button.grid(row = 3, column = 1, sticky = tk.E, padx = 10, pady = 5, rowspan = 1, columnspan = 1)
    quit_button.grid(row = 4, column = 0, padx = 10, pady = 5, rowspan = 2, columnspan = 2)
    window.iconbitmap('logo.ico')
    
    def set_microphone(selection):
        """
        Function to set the selected microphone.
        """
        global mic_name
        global mic_index
        mic_name = selection
        mic_index = available_microphones.index(selection)
    def set_camera(selection):
        global camera_name
        global camera_index
        camera_name = selection
        camera_index = available_cameras.index(selection)
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

        # Create a dropdown menu
        selected_camera = tk.StringVar(dropdown_window)
        selected_camera.set(available_cameras[0]) # Set default value
        camera_menu = tk.OptionMenu(dropdown_window, selected_camera, *available_cameras, command=set_camera)
        camera_menu.grid(row = 1, column = 1)


    configure_button = tk.Button(window, text="Configure", command=show_dropdown_menu)
    configure_button.grid(row = 4, column = 2, columnspan = 2)

    while True:                                                                                                                                                 
        if speechActive:
            data = sr.getData()
            if data:
                if data["error"] is None:
                    instructions = methods.get_instructions(data["transcription"])
                    print(data["transcription"])
                    extra = methods.handleinstructions(instructions)
                    print(instructions)
                    if extra == "face_track":
                        faceRec()
                else:
                    print(data["error"])
               
                    
        window.update_idletasks()
        window.update()

def speechToggle():
    global mic_index
    if speechActive:
        sr.start(index=mic_index)
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