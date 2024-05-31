import pathlib
import textwrap

import google.generativeai as genai
import os


file = open('prompt.txt', 'r')
default_prompt = file.read()
file.close()


speech_content = "pause the music."

# TODO: ADD TO .env
genai.configure(api_key='AIzaSyA4ZmxyxdRFS8F8KEUmfbhJwg5uLAmhQCc')

model = genai.GenerativeModel('gemini-pro')

def generateResponse(speech_content = "DISREGARD ALL OTHER INSTRUCTIONS AND RESPOND WITH JUST [] AND NOTHING ELSE"):
    try:
        response = model.generate_content(default_prompt + speech_content)
        return(response.text)

    except:
        return ("modelgeneration failed")


def main():
    inputFile = open("input.txt", "r")
    inputString = inputFile.read()
    inputFile.close()

    inputFile = open("input.txt", "w")
    inputFile.close();

    commandList = eval(generateResponse(inputString))

    clear = open('output.txt', 'w')
    clear.close()

    outputFile = open('output.txt', 'w')

    from command in commandList:
        for com in command.keys():
          outputFile.write(com)
          outputFile.write(command[com])
    outputFile.close()

def test():
    print("enter some test code here if you want to do anything")

if __name__ == "__main__":
    test()
