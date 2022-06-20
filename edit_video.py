import cv2
import os

for video in (os.listdir("demo_video")):

    cap = cv2.VideoCapture(os.path.join('demo_video', video))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("Video name: ", video)
    print("Frame rate: ", fps, "FPS")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    output = cv2.VideoWriter(os.path.join('edit_demo_video', video + ".avi"), fourcc, 5, (width, height))

    try:
        while(cap.isOpened()):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(fps) & 0xFF == ord('q'):
                    break
            output.write(frame)
    except:
        cap.release()
        cv2.destroyAllWindows() 