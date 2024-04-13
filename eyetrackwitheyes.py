from bs4 import Tag
import cv2
import numpy as np
import pyautogui
from screeninfo import get_monitors

detector = None
DEBUG = False
target_pos = (0,0)
pyautogui.FAILSAFE = False
def initDetector():
    global detector
    detector_params = cv2.SimpleBlobDetector_Params()
    # # Filter by Circularity
    # detector_params.filterByCircularity = True
    # detector_params.minCircularity = 0.8

    # # # Filter by Convexity
    # detector_params.filterByConvexity = True
    # detector_params.minConvexity = 0.6

    # # Filter by Inertia
    # detector_params.filterByInertia = False

    detector_params.filterByColor = True
    detector_params.blobColor = 0
    detector_params.filterByArea = True
    detector_params.maxArea = 1500

    detector = cv2.SimpleBlobDetector_create(detector_params)


def inRange(num1: int, num2: int, max_distance: int) -> bool:
    distance: int = abs(num1 - num2)
    return max_distance > distance


def displayAndWait(img):
    if DEBUG:
        cv2.imshow("my image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def cut_image(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    return img[eyebrow_h:height, 0:width]
def autistic_blob_process(img):
    old = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 45, 255, cv2.THRESH_BINARY)
    displayAndWait(img)
    xAverage =0
    yAverage = 0
    count = 0
    resolution = 1
    for y in range(0, img.shape[0], resolution):
        for x in range(0, img.shape[1], resolution):
            percentage = 1 - (img[y][x]/255)
            print(img[y][x])
            xAverage += percentage * x
            yAverage += percentage * y
            count += 1
    if count > 0:
        xAverage //= count
        yAverage //= count
    cv2.circle(old, (int(xAverage), int(yAverage)), 5, (255, 255, 0) , 1)
    displayAndWait(old)

def blob_process(img, detector,threshold):
    global target_pos
    if img is None:
        return []

    cv2.imshow("eye", img)
    displayAndWait(img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, img = cv2.threshold(img, 43, 255, cv2.THRESH_BINARY)
    displayAndWait(img)
    
    

    img = cv2.dilate(img, None, iterations=1)  # 2
    displayAndWait(img)

    img = cv2.medianBlur(img, 5)  # 3
    displayAndWait(img)

    keypoints = detector.detect(img)

    if len(keypoints) > 0:
        target_pos = (keypoints[0].pt[0], keypoints[0].pt[1])
    blank = np.zeros((1, 1))

    blobs = cv2.drawKeypoints(
        img, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    displayAndWait(blobs)

    return keypoints

def nothing(x):
    pass
def detect_eyes(img, threshold=45):
    global target_pos
    if detector is None:
        initDetector()

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

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
        target_pos = ((x + x + w)/2, (y + y + h)/2)
        
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    gray_face = gray_picture[y : y + h, x : x + w]  # cut the gray face frame out

    face = img[y : y + h, x : x + w]  # cut the face frame out

    eyes = eye_cascade.detectMultiScale(gray_face)

    eyes_matrix = []
    left_eye = None
    right_eye = None
    eye_found = False
    for i, (ex, ey, ew, eh) in enumerate(eyes):
        for ex2, ey2, ew2, eh2 in eyes[i + 1 :]:
            if inRange(ey2, ey, 20) and inRange(ew, ew2, 5) and inRange(eh, eh2, 5):
                cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 225, 255), 2)
                cv2.rectangle(
                    face, (ex2, ey2), (ex2 + ew2, ey2 + eh2), (0, 225, 255), 2
                )

                eyes_matrix.append((ex, ey, ew, eh))
                eyes_matrix.append((ex2, ey2, ew2, eh2))
                eye_found = True

                if ex < ex2:  # this is mirrored because the image is mirror I think
                    left_eye = face[ey2 : ey2 + eh2, ex2 : ex2 + ew2]
                    right_eye = face[ey : ey + eh, ex : ex + ew]
                else:
                    right_eye = face[ey2 : ey2 + eh2, ex2 : ex2 + ew2]
                    left_eye = face[ey : ey + eh, ex : ex + ew]
    eye_found = False#i cry but this is too hard.
    if(eye_found):
        left_eye = cut_image(left_eye)
        right_eye = cut_image(right_eye)
        # keypoints = autistic_blob_process(left_eye)

        keypoints = blob_process(left_eye, detector, threshold)

        cv2.drawKeypoints(
            left_eye,
            keypoints,
            left_eye,
            (0, 0, 255),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )

        keypoints = blob_process(right_eye, detector, threshold)

        cv2.drawKeypoints(
            right_eye,
            keypoints,
            right_eye,
            (0, 0, 255),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )
    displayAndWait(img)
    return img

def getMovement():
    print(target_pos)
    return ((target_pos[0]-384) * 5 + 540, (target_pos[1]-272) * 5 + 360)
def main():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    
    cv2.namedWindow('my image')
    cv2.createTrackbar('threshold', 'my image', 0, 255, nothing)
    while True:
        ret, frame = cap.read()
        # threshold = cv2.getTrackbarPos('threshold', 'my image')
        face_frame = detect_eyes(frame, 45)
        cv2.imshow("my image", face_frame)
        print(getMovement())
        pyautogui.moveTo(getMovement()[0], getMovement()[1])
        # cv2.imshow("my image", face_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
def test():
    DEBUG = True
    threshold = 45
    frame = cv2.imread("1_Y-o6h7cu_WrNGWRPQZ-moQ.png")

    detect_eyes(frame, threshold)

if __name__ == "__main__":
    for m in get_monitors():
        print(str(m))
    main()
    
    # test()
