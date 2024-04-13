import pyautogui as pg
import time
import os
import facetrack
from PyQt5.QtWidgets import QApplication
import sys
# mouseInfo = pg.position()
# print(mouseInfo)

#FUNCTIONS returns current mouse position, takes you to particular position, left and right click, keyboard input
# open app, 
pg.FAILSAFE = False
RUNNING_FACEDETECTION = False
def setup():
    global screenHeight, screenWidth, dpi
    screenWidth, screenHeight = pg.size() 
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
def startFaceTrack():
    RUNNING_FACEDETECTION = True
    facetrack.start()

def pauseFaceTrack():
    RUNNING_FACEDETECTION = False
    facetrack.end()

def moveToFace():
    pg.moveTo(facetrack.getMovement(screenWidth, screenHeight)[0], facetrack.getMovement(screenWidth, screenHeight)[1])
def write(string: str):
    indent: bool = False
    if "\t" in string:
        tabs = string.split("\t")
        indent = True
    elif "\n" in string:
        tabs = string.split("\n")
        indent = False
    else:
        indent = None
    if indent is None:
        pg.write(string, 0.01)
    elif indent is False:
        for s in tabs:
            pg.write(s, 0.01)
            pg.press("enter")
    elif indent is True:
        for s in tabs:
            pg.write(s, 0.01)
            pg.press("tab")
def moveMouse(inch:float):
    global dpi
    dist = inch * dpi
    x,y = pg.position()
    pg.moveTo(x+dist,y)

def copy():
    pg.hotkey("ctrl", "c")
def paste():
    pg.hotkey("ctrl", "v")
def undo():
    pg.hotkey("ctrl", "z")
def goback():
    pg.hotkey("ctrl","shift", "left")    
def goforward():
    pg.hotkey("ctrl","shift", "right") 
def bold():
    pg.hotkey("ctrl","b")   
def delete():
    pg.hotkey("ctrl", "delete")
def newtab():
    pg.hotkey("ctrl", "t")
def leftClick():
    pg.click()

def leftClick(x, y):
    pg.click(x, y, duration = 0.1)
def doubleClick():
    pg.doubleClick()
def rightClick():
    pg.rightClick()

def middleClick():
    pg.middleClick()
    
def scroll(amount):
    pg.scroll(amount)
    
def goToPosition(x, y):
    pg.moveTo(x, y, duration = 0.1)

def pressKey(name):
    pg.press(name)
def openApp(name):
    pg.press("win")
    time.sleep(0.5)
    pg.write(name, 0.01)
    pg.press("enter")

def handleinstructions(instructions):
    global RUNNING_FACEDETECTION
    for dict in instructions:
        for key, value in dict.items():
            match key:
                case "click":
                    if value == "double":
                        doubleClick()
                    elif value == "left":
                        leftClick()
                    elif value == "right":
                        rightClick()
                case "write":
                    write(value)
                case "toggle_mouse_movement":
                    if RUNNING_FACEDETECTION:
                        pauseFaceTrack()
                    else:
                        startFaceTrack()
                    RUNNING_FACEDETECTION = not RUNNING_FACEDETECTION

def main():
    setup()
    openApp("google")

if __name__ == "__main__":
    main()