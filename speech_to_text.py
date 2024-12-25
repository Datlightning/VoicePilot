import random
import re
import time
from unittest import skip
import methods
import speech_recognition as sr
import translator
import threading as t
# recognize() gets a command. function LOOPS 
# param @timetospeak = the amount of time that you get to sleep. 
# returns: a string if it works, 1 or 2 for errors. 
# hope to not get an error ig lol. 
data = []
addition = False
skipRecalibrate = False
def recognize(recognizer, microphone):
    global skipRecalibrate
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    try: 
        with microphone as source:
            if (not skipRecalibrate):
                recognizer.adjust_for_ambient_noise(source, .5)
            audio = recognizer.listen(source, timeout = 0.5, phrase_time_limit=5.2)
            
    except: 
        skipRecalibrate = True
        response = {
            "success": False,
            "error": "Empty Source",
            "transcription": ""
        }
        return response


    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response = {
            "error": None,
            "transcription": recognizer.recognize_google(audio)
        }
    except sr.RequestError:
        # API was unreachable or unresponsive
        response = {
            "error": "API is unreachable",
            "transcription": ""
        }
    except sr.UnknownValueError:
        # speech was unintelligible
        response = {
            "error": "Speech Was Unintelligible",
            "transcription": ""
        }
    
    return response
def getData():
    global data
    global addition
    if data:
        addition = False
        return data.pop(0)
    
def getChange():
    global addition
    return addition
def listen(d_index: int = 0):
    global data
    global addition
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=d_index)
    while on:
        data.append(recognize(recognizer=recognizer, microphone=microphone))
        addition = True
def start(index: int = 0):
    global on
    on = True
    x = t.Thread(target=lambda: listen(d_index=index), daemon = True)
    x.start()
def end():
    global on
    on = False
def getmics():
    for i,mic in enumerate(sr.Microphone.list_microphone_names()):
        print(i,mic)
def main(): 
    # getmics()
    # print(sr.Microphone.list_microphone_names())
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=7)
    while True:
        print(recognize(recognizer, microphone)["transcription"])


if __name__ == "__main__": 
    main()
    