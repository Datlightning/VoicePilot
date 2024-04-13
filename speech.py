import random
import time

import speech_recognition as sr

# recognize() gets a command. function LOOPS 
def recognize(recognizer, microphone):
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
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, .1)
        # TIMEOUT = the second param
        # time to listen = the third param: i thought that three seconds would be good. 
        audio = recognizer.listen(source, .2, 3)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": ""
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        print("network error")
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        print("could not understand what you were saying fool")
        response["error"] = "Unable to recognize speech"
    
    return response["transcription"].lower()

def rec():
    # set the list of words, maxnumber of guesses, and prompt limit
    
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    
    # format the instructions string
    
    # show instructions and wait 3 seconds before starting the game
    currentPhrase = []
    print("currently recognizing")
    run = True
    while run:  
        name = "command"
        currentWord = recognize(recognizer, microphone)
        currentPhrase = currentPhrase + currentWord.split() 
        
        i = 0
        firstOcc = False
        first = 0
        for word in currentPhrase: 
            
            if word == name:
                first = i
                firstOcc = True
                try: 
                    currentPhrase = currentPhrase[i+1:]
                    break 
                except: 
                    pass
            i += 1
            
        if firstOcc:
            i = 0 
            found = False
            
            for word in currentPhrase: 
                if word == name: 
                    try: 
                        currentPhrase = currentPhrase[first:i]
                        found = True 
                        break 
                    except: 
                        pass
                    
                i += 1
            if found: 
                final = currentPhrase
                currentPhrase = []
                
                
                return (" ".join(final))
                run = False 
                
            else: 
                print("second command not found") 
        else: 
            print("first command not found") 
        currentPhrase = []
            
        
        
        
        

    # if there was an error, stop the game
    
    # show the user the transcription
    
    # determine if guess is correct and if any attempts remain
    
    # determine if the user has won the game
    # if not, repeat the loop if user has more attempts
    # if no attempts left, the user loses the game
    