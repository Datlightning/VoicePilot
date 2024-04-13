import pathlib
import textwrap

import google.generativeai as genai


file = open('input.txt', 'r')
default_prompt = file.read()
file.close()

speech_content = "move the mouse write 3 inches"


genai.configure(api_key='AIzaSyB8ZaFbYi_u2nfO-NI1D8YNTCvUofDqkPs')

model = genai.GenerativeModel('gemini-pro')

def generateResponse(speech_content = "DISREGARD ALL OTHER INSTURCTIONS AND RESPOND WITH JUST [] AND NOTHING ELSE"):
    try:
        response = model.generate_content(default_prompt + speech_content)
        return(eval(response.text))
    
    except:
        return ([])


if __name__ == "__main__":
    print(generateResponse(speech_content))