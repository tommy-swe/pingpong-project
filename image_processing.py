import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

cap = cv2.VideoCapture('video_data/twosize_5.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frame rate: ", int(fps), "FPS")


def segment_by_color(img):
    hei, wid= img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    #ball segmentation
    light_orange = (1, 150, 150)
    dark_orange = (15, 255, 255)
    mask_orange = cv2.inRange(hsv, light_orange, dark_orange)

    #table segmentation
    light_blue = (110, 100, 100)
    dark_blue = (150, 255, 255)
    
    mask_blue = cv2.inRange(hsv, light_blue, dark_blue)
    final_mask = mask_orange

    result = cv2.bitwise_and(img, img, mask=final_mask)
    return result, final_mask

def bigget_countours(img, mask):

    ret, thresh = cv2.threshold(mask, 40, 255, 0)     
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

    # draw the biggest contour (c) in green
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img


def draw_color_hist(img):
    b, g, r = cv2.split(img) #h s v
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    # axis.set_xlabel("Red")
    # axis.set_ylabel("Green")
    # axis.set_zlabel("Blue")
    axis.set_zlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_xlabel("Value")
    plt.show()
    # plt.pause(0.1)


size = (640, 480)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
output = cv2.VideoWriter('twosize_5.avi', fourcc, fps, size)

try:
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        re_frame = cv2.resize(frame, size, interpolation = cv2.INTER_AREA)
        out, mask = segment_by_color(re_frame)
        # table_with_contours = bigget_countours(out, mask)
        # draw_color_hist(out)

        cv2.imshow('frame', out)
        #   cv2.waitKey(10)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        # output.write(out)
except:
    cap.release()
    cv2.destroyAllWindows()