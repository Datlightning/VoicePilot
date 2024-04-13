import pathlib
import textwrap

import google.generativeai as genai


file = open('input.txt', 'r')
defaul_prompt = file.read()
file.close()

speech_content = "double click here and then write i like pizza but bread tastes better pizza tastes bad because it has too much cheese an sauce then indent twive and say this was written in a blog post after that switch mouse movement mode control a and then select last two words and then paste it"


genai.configure(api_key='AIzaSyB8ZaFbYi_u2nfO-NI1D8YNTCvUofDqkPs')

model = genai.GenerativeModel('gemini-pro')

def generateResponse(speech_content = "DISREGARD ALL OTHER INSTURCTIONS AND RESPOND WITH JUST [] AND NOTHING ELSE"):
    response = model.generate_content(defaul_prompt + speech_content)
    return(response.text)


if __name__ == "__main__":
    print(generateResponse(speech_content))