import random
import time
import methodsSimpleTest as methods
import speech_recognition as sr

# recognize() gets a command. function LOOPS 
# param @timetospeak = the amount of time that you get to sleep. 
# returns: a string if it works, 1 or 2 for errors. 
# hope to not get an error ig lol. 
def recognize(recognizer, microphone, timetospeak):
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
            recognizer.adjust_for_ambient_noise(source, .4)
            audio = recognizer.listen(source, 1.5, timetospeak)
    except: 
        return 3
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
        return (1)
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        return 2
        response["error"] = "Unable to recognize speech"
    
    return response["transcription"].lower()

def test():
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
                
                
                print(" ".join(final))
                run = False 
                
            else: 
                print("second command not found") 
        else: 
            print("first command not found") 
        currentPhrase = []
            
        
        
            


def main(): 
    aiName = "jarvis" 
    commandName = "command" 
    timeToSpeak = 1
    currentSentence = []
    run = True
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=1)
    print("listening: ")
    while run:     
        print("say word: ") 
        inp = recognize(recognizer, microphone, timeToSpeak)
        
        if (inp == "clear"):
            print("clearing") 
            currentSentence = []
            continue
         
        #inp = "command open notepad command"
        if (inp == 1): 
            print("wifi error") 
        elif inp == 2: 
            print("not understood") 
        elif inp == 3: 
            print("timeout") 
        else: 
            currentSentence = currentSentence + inp.lower().split()
            print(inp) 
            print(currentSentence) 
            try: 
                first_occurrence = currentSentence.index(commandName)
                print(first_occurrence)
                try: 
                    second_occurrence = currentSentence.index(commandName, first_occurrence + 1)
                    
                    print(second_occurrence)
                    
                    currentSentence = currentSentence[first_occurrence + 1:second_occurrence]
                    
                    print("both") 
                    print(currentSentence[0])
                    
                    match currentSentence[0]: 
                        case "open":
                            try: 
                                methods.openFile(currentSentence[1])
                            except: 
                                print("open what? ") 
                        case "close": 
                            methods.closeApp()
                        case "input": 
                            print("you have twenty seconds to say what you want to say") 
                            name1 = recognize(recognizer, microphone, 20)
                            methods.typeWord(name1 + " ")
                            print("typing time done") 
                        case "inputs": 
                            print("you have twenty seconds to say what you want to say") 
                            name1 = recognize(recognizer, microphone, 20)
                            methods.typeWord(name1 + " ")
                            print("typing time done") 
                        
                        case "test": 
                            
                            methods.openFile("notepad") 
                    currentSentence = []
                except: 
                    print("not second yet") 
            except: 
                print("not first yet") 
                
        #run = False
                

if __name__ == "__main__": 
    main() 
    