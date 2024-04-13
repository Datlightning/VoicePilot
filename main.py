import speech_recognition as sr
import pyttsx3




def main(): 
    recognizer = sr.Recognizer() 
    while True: 
        try: 
            with sr.Microphone() as mic: 
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic) 
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print("text: " + text)
                
        except sr.UnknownValueError(): 
            print("oh no") 
            
    return 1 


if __name__ == "__main__":
    main()