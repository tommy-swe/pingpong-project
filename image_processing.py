import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import colors
import imutils

def unique_count_app(a):
    colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]

def detect_table_Color(img):

    height,width = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    most_dominant_color = unique_count_app(hsv)
    # h, s, v = cv2.split(hsv)
   
    #table segmentation
    # light_blue = (105, 70, 70) 
    # dark_blue = (128, 255, 255)
    light_blue = np.array(most_dominant_color) - np.array([5, 100, 100])
    dark_blue = np.array(most_dominant_color) + np.array([5, 50, 50])
    
    mask_blue = cv2.inRange(hsv, light_blue, dark_blue)
  
    # final_mask = mask_orange + mask_blue #segment table and ball
    final_mask = mask_blue # segment only table
  
   
    final_mask = cv2.medianBlur(final_mask, ksize = 11)
    pesudo_mask = np.zeros((height,width), np.uint8)

    #draw contours        
    contours, hierarchy = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea)
        hull = cv2.convexHull(c, False)
        cv2.drawContours(pesudo_mask, [hull], 0, 255, -1)
    
    result = cv2.bitwise_and(img, img, mask=pesudo_mask)
    if len(contours) != 0:
        # draw in blue the contours that were founded
        # cv2.drawContours(result, contours, -1, (255, 255, 0), 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        cv2.drawContours(result, [c], 0, (255, 125, 255), 3)
        cv2.drawContours(result, [hull], 0, (255, 0, 255), 3)
        x,y,w,h = cv2.boundingRect(c)

    # draw the biggest contour (c) in green
    cv2.rectangle(result,(x,y),(x+w,y+h),(255, 128, 128),2)
  
    return result, final_mask, [x, y, w, h]

def net_detect(img, rec):

    output = img.copy()
    x, y, w, h = rec
    p1x = x + w//2
    p1y = y
    p2x = x + w//2
    p2y = y + h
    cv2.line(output, (p1x, p1y), (p2x, p2y), (0, 255, 0), 3)

    return output



def ball_in_table_detect(img, mask, bg_mask):

    output = img.copy()
    ball_segment = mask - bg_mask
    contours, hierarchy = cv2.findContours(ball_segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # find the biggest countour (c) by the area
        cv2.drawContours(output, contours, -1, (255, 255, 0), 3)
        c = max(contours, key = cv2.contourArea)
        cv2.drawContours(output, [c], 0, (255, 128, 128), -1)
        x,y,w,h = cv2.boundingRect(c)

    return output

def detect_ball_general(img):
    

    greenLower = (5,50,50)
    greenUpper = (15,255,255)

    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    frame = img.copy()
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = min(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
    return frame


def detect_ball_Houghtransform(img, mask, rec):

    # Creating kernel
    x, y, w, h = rec
    erosion_size = 7
    element = cv2.getStructuringElement(2, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))
    
    output = img.copy()
    ball_segment = mask.copy()
    
    ball_segment = cv2.erode(ball_segment, element)
    # cv2.imshow("mask", ball_segment)
    # cv2.waitKey(0)

    detected_circles = cv2.HoughCircles(ball_segment, 
                   cv2.HOUGH_GRADIENT, 1, 50, param1 = 80,
               param2 = 10, minRadius = 1, maxRadius = 50)

    c = []
    ball_to_net = []
    if detected_circles is not None:
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
    
        detected_circles = detected_circles[0, :]
        detected_circles = detected_circles[detected_circles[:, 2].argsort()]
        for pt in detected_circles:
            a, b, r = pt[0], pt[1], pt[2]
            #calculate the length to net
            ball_to_net.append(abs(a - (x + w//2)))
            # Draw the circumference of the circle.
            cv2.circle(output, (a, b), r, (255, 255, 0), -1)
        
        ball_to_net = np.array(ball_to_net)
        detected_circles = detected_circles[ball_to_net.argsort()]
        c = detected_circles[0]
        cx, cy = c[0], c[1]
        #check ball inside table boundary
        if((cx > x and cx < x + w) and (cy > y and cy < y + h)):
            cv2.circle(output, (c[0], c[1]), c[2] // 2, (0, 0, 255), -1)
        else:
            c = []

    return output, c

def draw_trajectory(img, trajectory):
     
    output = img.copy()
    n = len(trajectory)
    if(n > 1):
        for i in range(max(0, n - 4), n - 1):
            a1, b1, r1 = trajectory[i]
            a2, b2, r2 = trajectory[i+1]
            if(r1 == 0):
                continue
            #interpolate 1 missing point
            elif(r1 > 0 and r2 == 0):
                try:
                    a3, b3, r3 = trajectory[i+2]
                   
                    if(r3 > 0):
                        a2 = (a1 + a3) // 2
                        b2 = (b1 + b3) // 2
                    else: continue   
                except: continue
            cv2.circle(output, (a1, b1), 4, (255, 255, 255), -1)
            if(b2 > b1):
                cv2.line(output, (a1, b1), (a2, b2), (0, 255, 0), 2)
            else:
                cv2.line(output, (a1, b1), (a2, b2), (0, 165, 255), 2)
    return output


def draw_score(img, score):

    output = img.copy()
    h, w = output.shape[:2]
    cv2.putText(output, str(score["L"]), (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, 2)
    cv2.putText(output, str(score["R"]), (w - 30, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, 2)
    return output

def scoring(img, trace, rec, score, fps, reset):
 
    n_frames = 2 * fps #strat couting from nth frame and consider n frames to get the score
    n = len(trace)
  
    if(n > n_frames): #at the begining frames, dont do any action, wait until the first n frames has passed -> to get enough information
        trace = np.array(trace) # you can interpolate some missing balls -> but not solve yet
        xc, yc, rc = trace[-1] #current frame ball pos

        net = rec[0] + rec[2] // 2
        decision_frames = trace[(-n_frames-1):-1] #get n frames for scoring decision
        rp = np.sum(decision_frames)

        if(rc > 0 and rp == 0):  #long pause = no ball afer n frames and has ball at the current frame
            reset = True         # after long pause, initialize new set

        side_array = {"OUT": 0, "R": 0, "L": 0} # couting all ball positions in decision frames and divide into 3 case: L side, R side or OUT
        for i in range(n_frames):
            x_axis = decision_frames[i][0]
            if(x_axis == 0): side_array["OUT"] += 1 #ball side is decided by correlation between ball and net
            elif(x_axis > net): side_array["R"] += 1
            else: side_array["L"] += 1

        print(side_array)
        print(reset)

        if(reset == True): # if newset is on, you can decide the score,
                           # if newset is off, that means you already scored last set and the ball is OUT so you dont consider these frames
            if(side_array["L"] > n_frames / 1.2): score["R"] += 1; reset = False # If the ball stuck in L side, give a score to right side
            if(side_array["R"] > n_frames / 1.2): score["L"] += 1; reset = False # If the ball stuck in R side, give a score to left side
            if(side_array["OUT"] == n_frames - 1): # If the ball stuck in OUT side, check the final state and give the socre
                a, b, r = decision_frames[0]
                if(r > 0):
                    if(a < net): score["L"] += 1
                    else: score["R"] += 1
                    reset = False
   

    output = draw_score(img, score)

    return output, score, reset

    



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

import os

if __name__ == "__main__":

    for video in (os.listdir("high_quality_video")):

        if(int(video.split(".")[0]) < 28): # check video file name
            continue

        cap = cv2.VideoCapture(os.path.join('high_quality_video', video))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print("Video name: ", video)
        print("Frame rate: ", fps, "FPS")

        size = (640, 480)
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        # output = cv2.VideoWriter('half_table_middle.avi', fourcc, fps, size)
        output = cv2.VideoWriter(os.path.join('high_quality_result_video', video + ".avi"), fourcc, 10, size)

        flag = 0 #initiate some scores
        trajectory = []
        score = {"L": 0, "R": 0}
        reset = True
        try:
            while(cap.isOpened()):
                ret, frame = cap.read()
            
                re_frame = cv2.resize(frame, size, interpolation = cv2.INTER_AREA)
                out, mask, rec = detect_table_Color(re_frame) #for speeding up, we only detect table after some frames.
                if(flag == 0):
                    mask_bg = mask
                    flag += 1
                table_with_net = net_detect(out, rec)

                table_with_ball, c = detect_ball_Houghtransform(table_with_net, mask, rec)
                # draw_color_hist(out)
                if(len(c) > 0):
                    trajectory.append(c)     
                else:
                    trajectory.append(np.array([0, 0, 0]))
                # print(trajectory)
                table_with_ball = draw_trajectory(table_with_ball, trajectory)
                
                table_with_score, score, reset = scoring(table_with_ball, trajectory, rec, score, fps, reset)
                
                cv2.imshow('contours',  table_with_score)
                cv2.imshow('mask', mask)
                cv2.imshow('frame', re_frame)
                    #   cv2.waitKey(10)qq
                if cv2.waitKey(0) & 0xFF == ord('q'):
                    break
                output.write(table_with_score)
        except:
            cap.release()
            cv2.destroyAllWindows() 