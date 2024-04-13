import pyautogui as pg
import time
import os

# mouseInfo = pg.position()
# print(mouseInfo)

#FUNCTIONS returns current mouse position, takes you to particular position, left and right click, keyboard input
# open app, 

def setup():
    global screenHeight, screenWidth
    screenWidth, screenHeight = pg.size()    

def getCurrentMousePosX():
    x, y = pg.position()
    return x

def getCurrentMousePosY():
    x, y = pg.position()
    return y
    
def leftClick():
    pg.click()

def leftClick(x, y):
    pg.click(x, y, duration = 0.1)

def rightClick():
    pg.rightClick()

def middleClick():
    pg.middleClick()
    
def scroll(amount):
    pg.scroll(amount)
    
def goToPosition(x, y):
    pg.moveTo(x, y, duration = 0.1)

def pressKey(name):
    pg.press(name);
    
def openFile(name): 
    pg.press("win")
    time.sleep(.2)
    pg.typewrite(name)
    time.sleep(.2)    
    pg.press("enter") 

def closeApp(): 
    pg.hotkey('alt', 'f4')  
    
    
def typeWord(phrase): 
    pg.typewrite(phrase)

def main():
    # print(pg.position())
    # print(getCurrentMousePos())
    # pg.alert('this is an alert')
    # pg.moveTo(100, 150, duration = 0.5)
    goToPosition(50, 100)
    pressKey('d')

def changeApp(): 
    pg.hotkey('alt', 'tab')  
    

if __name__ == "__main__":
    main()