import ipywidgets as widgets
from IPython.display import display
from queue import Queue
from threading import Thread

messages = Queue()
recordings = Queue()

record_button = widgets.Button(
    description='Record',
    disabled=False,
    button_style='success',
    tooltip='Record',
    icon='microphone'
)

stop_button = widgets.Button(
    description='Stop',
    disabled=False,
    button_style='warning',
    tooltip='Stop',
    icon='stop'
)

output = widgets.Output()

def start_recording(data):
    messages.put(True)
    
    with output:
        display("Starting...")
        record = Thread(target=record_microphone)
        record.start()
        transcribe = Thread(target=speech_recognition, args=(output,))
        transcribe.start()

def stop_recording(data):
    with output:
        messages.get()
        display("Stopped.")
    
record_button.on_click(start_recording)
stop_button.on_click(stop_recording)

display(record_button, stop_button, output)