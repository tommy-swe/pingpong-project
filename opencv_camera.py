import cv2
import os

cam = cv2.VideoCapture(0)
fps = int(cam.get(cv2.CAP_PROP_FPS))
print("Frame rate: ", fps, "FPS")


if (cam.isOpened() == False): 
    print("Error reading video file")

else:
    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
    size = (frame_width, frame_height)
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    output = cv2.VideoWriter("test.avi", fourcc, 10, size)

    while True:
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if k != -1:
            break
        output.write(image)

    cam.release()
    cv2.destroyAllWindows()