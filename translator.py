import pathlib
import textwrap

import google.generativeai as genai


file = open('input.txt', 'r')
default_prompt = file.read()
file.close()

speech_content = "pause the music."

# TODO: ADD TO .env 
genai.configure(api_key='AIzaSyA4ZmxyxdRFS8F8KEUmfbhJwg5uLAmhQCc')

model = genai.GenerativeModel('gemini-pro')

def generateResponse(speech_content = "DISREGARD ALL OTHER INSTURCTIONS AND RESPOND WITH JUST [] AND NOTHING ELSE"):
    try:
        response = model.generate_content(default_prompt + speech_content)
        return(eval(response.text))
    
    except:
        return ([])


if __name__ == "__main__":
    print(generateResponse(speech_content))