import pathlib
import textwrap

import google.generativeai as genai


file = open('input.txt', 'r')
defaul_prompt = file.read()
file.close()

speech_content = "Left click here and then write happy birthday jacob, then go down two lines and say from brandon"

genai.configure(api_key='AIzaSyB8ZaFbYi_u2nfO-NI1D8YNTCvUofDqkPs')

model = genai.GenerativeModel('gemini-pro')

def main():
    response = model.generate_content(defaul_prompt + speech_content)
    print(response.text)


if __name__ == "__main__":
    main()