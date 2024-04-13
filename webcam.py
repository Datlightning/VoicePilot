import cv2

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    check, frame = cam.read()
    print(check)
    if not check:
        break
    cv2.normalize(frame, frame, 80, 255, cv2.NORM_MINMAX)

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()