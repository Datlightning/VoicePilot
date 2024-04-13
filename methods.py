import pyautogui as pg
import time
import facetrack
from PyQt5.QtWidgets import QApplication
import sys
import translator
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
def moveMouse(x:float, y:float):
    global dpi
    dist = x * dpi
    ydist = y*dpi
    x,y = pg.position()
    pg.moveRel(dist, ydist)

def copy():
    pg.hotkey("ctrl", "c")
def paste():
    pg.hotkey("ctrl", "v")
def undo():
    pg.hotkey("ctrl", "z")

def gobackhighlight():
    pg.hotkey("ctrl","shift", "left")    
def goforwardhighlight():
    pg.hotkey("ctrl","shift", "right") 
def goback():
    pg.hotkey("ctrl", "left")    
def goforward():
    pg.hotkey("ctrl","right") 
def bold():
    pg.hotkey("ctrl","b")   
def underline():
    pg.hotkey("ctrl","u")   
def ital():
    pg.hotkey("ctrl","i")  
def cut():
    pg.hotkey("ctrl", "x") 
def selectall():
    pg.hotkey("ctrl","a")   
def delete():
    pg.hotkey("ctrl", "delete")
def newtab():
    pg.hotkey("ctrl", "t")

def switchbrowsertab():
    pg.hotkey("ctrl", "tab")
def taskbarWIN():
    pg.hotkey("win", "t")
def screenshot(): 
    pg.hotkey("win", "shift", "s")
def calendarToggle11(): 
    pg.hotkey("win",  "n")
def openAccessibilitySettings(): 
    pg.hotkey("win",  "u")
def switchTab(): 
    pg.hotkey("alt",  "tab")
def close():
    pg.hotkey("alt", "f4")
def leftClick():
    pg.click()
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
    time.sleep(.5)
    pg.write(name, 0.01)
    pg.press("enter")
    time.sleep(.2)

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
                case "press":
                    pressKey(value)

                case "write":
                    write(value)
                case "toggle_mouse_movement":
                    if value == "toggle":
                        if RUNNING_FACEDETECTION:
                            pauseFaceTrack()
                        else:
                            startFaceTrack()
                    elif len(value) == 2:
                    
                        match value[0]:
                            case "right":
                                moveMouse(float(value[1]), 0)
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "left":
                                moveMouse(-1 * float(value[1]), 0)
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "up":
                                moveMouse(0, float(value[1]))
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "down":
                                moveMouse(0, -1 * float(value[1]))
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "top_right":
                                val = float(value[1])/(2**(0.5))
                                moveMouse(val, val)

                            case "bottom_right":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(val, -val)
                            case "top_left":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(-val, val)
                            case "bottom_left":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(-val, -val)
                    RUNNING_FACEDETECTION = not RUNNING_FACEDETECTION
                case "move_mouse":
                    match value[0]:
                            case "right":
                                moveMouse(float(value[1]), 0)
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "left":
                                moveMouse(-1 * float(value[1]), 0)
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "up":
                                moveMouse(0, float(value[1]))
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "down":
                                moveMouse(0, -1 * float(value[1]))
                                print("BEEP BEEP IM MOVING DA MOUSE")
                            case "top_right":
                                val = float(value[1])/(2**(0.5))
                                moveMouse(val, val)

                            case "bottom_right":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(val, -val)
                            case "top_left":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(-val, val)
                            case "bottom_left":
                                val = int(value[1])/(2**(0.5))
                                moveMouse(-val, -val)
                case "select_command":
                    match value:
                        case "backward":
                            gobackhighlight()
                        case "forward":
                            goforwardhighlight()
                case "open":
                    openApp(value)
                case "command":
                    match value:
                        case "new_tab":
                            newtab()
                        case "copy":
                            copy()
                        case "paste":
                            paste()
                        case "bold":
                            bold()
                        case "italicize":
                            ital()
                        case "underline":
                            underline()
                        case "forward_word":
                            goforward()
                        case "back_word":
                            goback()
                        case "all":
                            selectall()
                        case "undo":
                            undo()
                        case "close":
                            close()
                        case "cut":
                            cut()
                        case "switch_window":
                            switchTab() 
                        case "switch_tab": 
                            switchbrowsertab()
                        

                        
                        
                        

def get_instructions(prompt):
        instructions = translator.generateResponse(prompt)
        return instructions
def main():
    moveMouse(1.0, 2.0)
if __name__ == "__main__":
    main()