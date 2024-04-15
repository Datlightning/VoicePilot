import cv2
import numpy as np
import pyautogui
from screeninfo import get_monitors
import time
import threading as t

DEBUG = False
target_pos = (0,0)
on = False

def inRange(num1: int, num2: int, max_distance: int) -> bool:
    distance: int = abs(num1 - num2)
    return max_distance > distance
def displayAndWait(img):
    if DEBUG:
        cv2.imshow("my image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def detect_face(img):
    global target_pos
    
    img = cv2.flip(img,1)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # make picture gray
    # find the biggest face on the screen.
    faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)
    max_x = 0
    max_y = 0
    big_face = [[0,0], [0,0]]
    for x, y, w, h in faces:
        if x + w > max_x and y + h > max_y:
            max_x = x + w
            max_y = y + h
            big_face[0] = [y, h]
            big_face[1] = [x, h]
    y, h = big_face[0]
    x, w = big_face[1]
    if len(faces) > 0:
        target_pos = ((x + x + w)/2 * .60 + target_pos[0] * .40, (y + y + h)/2 * .60 + target_pos[1] * .40)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    return img

def getMovement(width: int, height: int) -> tuple:
    return ((target_pos[0]-300) * 5.5 + width//2, (target_pos[1]-272) * 7 + height//2)
def thread():
    global on
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    m = get_monitors()[0]
    screenWidth = m.width
    screenHeight = m.height
    while on:
        _, frame = cap.read()
        face_frame = detect_face(frame)
        pyautogui.moveTo(getMovement(screenWidth, screenHeight)[0], getMovement(screenWidth, screenHeight)[1])
        # cv2.imshow("facial detection", newframe)

    cap.release()
def start():
    global on
    on = True
    x = t.Thread(target=thread, daemon = True)
    x.start()
def end():
    global on
    on = False
def main():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    m = get_monitors()[0]
    screenWidth = m.width
    screenHeight = m.height
    cv2.namedWindow('my image')
    while True:
        ret, frame = cap.read()
        # threshold = cv2.getTrackbarPos('threshold', 'my image')
        face_frame = detect_face(frame)
        cv2.imshow("my image", face_frame)
        # print(getMovement(screenWidth, screenHeight))
        pyautogui.moveTo(getMovement(screenWidth, screenHeight)[0], getMovement(screenWidth, screenHeight)[1])

        # cv2.imshow("my image", face_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    main()
    
    # test()
