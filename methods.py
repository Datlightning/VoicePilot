import pyautogui as pg
import time

mouseInfo = pg.position()
print(mouseInfo)

#FUNCTIONS returns current mouse position, takes you to particular position, left and right click, keyboard input
# open app, 

# def currentMousePos():
    

def main():
    pg.mouseinfo()
    pg.alert('this is an alert')
    pg.moveTo(100, 150, duration = 1)

if __name__ == "__main__":
    main()