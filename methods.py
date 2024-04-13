from importlib.util import decode_source
from tkinter import Menu
import pyautogui as pg
import time
<<<<<<< Updated upstream
import os
=======
import facetrack
from screeninfo import get_monitors
from PyQt5.QtWidgets import QApplication
import sys
>>>>>>> Stashed changes

# mouseInfo = pg.position()
# print(mouseInfo)

#FUNCTIONS returns current mouse position, takes you to particular position, left and right click, keyboard input
# open app, 
pg.FAILSAFE = False
def setup():
    global screenHeight, screenWidth, dpi
    screenWidth, screenHeight = pg.size() 
    app = QApplication(sys.argv)
    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()
def startFaceTrack():
    facetrack.start()

def pauseFaceTrack():
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

def main():
    # print(pg.position())
    # print(getCurrentMousePos())
    # pg.alert('this is an alert')
    # pg.moveTo(100, 150, duration = 0.5)
    setup()
    moveMouse(2)

if __name__ == "__main__":
    main()