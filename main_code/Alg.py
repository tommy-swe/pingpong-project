## Author: Dang Thanh Vu & Tokhirjon Turgunov(Tommy)
## Date: 2022.09

# this script is for main algorithm of PingPong project

import numpy as np
import cv2


def unique_count_app(a):
    colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]

def draw_score(img, score):

    h, w = img.shape[:2]
    cv2.putText(img, str(score["L"]), (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, 2)
    cv2.putText(img, str(score["R"]), (w - 30, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, 2)
  
def draw_trajectory(img, trajectory):
     
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
            cv2.circle(img, (a1, b1), 4, (255, 255, 255), -1)
            if(b2 > b1):
                cv2.line(img, (a1, b1), (a2, b2), (0, 255, 0), 2)
            else:
                cv2.line(img, (a1, b1), (a2, b2), (0, 165, 255), 2)

class PingPongAlg:
    def __init__(self, fps, isdraw=False, isshow=False, issave=False) -> None:
        self.ball_trajectory = []
        self.isdraw = isdraw
        self.isshow = isshow
        self.issave = issave

        self.fps = fps
        self.score = {"L": 0, "R": 0}
        self.reset = True
        self.base_size = (640, 480)

        self.curent_frame = None
        self.result_img = None
        pass

    def table_detection(self, frame):
        
       
        self.curent_frame = cv2.resize(frame, self.base_size, interpolation = cv2.INTER_AREA)
        height,width = self.base_size
        hsv = cv2.cvtColor(self.curent_frame, cv2.COLOR_BGR2HSV)
        # h, s, v = cv2.split(hsv)

        #table segmentation
        most_dominant_color = unique_count_app(hsv)
        light_blue = np.array(most_dominant_color) - np.array([5, 100, 100])
        dark_blue = np.array(most_dominant_color) + np.array([5, 50, 50])
        # light_blue = (105, 70, 70)
        # dark_blue = (128, 255, 255)
    
        mask_blue = cv2.inRange(hsv, light_blue, dark_blue)
        final_mask = cv2.medianBlur(mask_blue, ksize = 11)

        #draw contours        
        contours, hierarchy = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) != 0:
            c = max(contours, key = cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)

        if(self.isdraw == True):
            if len(contours) != 0:
                pesudo_mask = np.zeros((width, height), np.uint8)
                
                # find the biggest countour (c) by the area
                c = max(contours, key = cv2.contourArea)
                hull = cv2.convexHull(c, False)
                cv2.drawContours(pesudo_mask, [hull], 0, 255, -1)
    
                result = cv2.bitwise_and(self.curent_frame, self.curent_frame, mask=pesudo_mask)
               
                #draw biggest contour
                cv2.drawContours(result, [c], 0, (255, 125, 255), 3)
                #draw convex hull
                cv2.drawContours(result, [hull], 0, (255, 0, 255), 3)
                x,y,w,h = cv2.boundingRect(c)
                # draw the rect boundary
                cv2.rectangle(result,(x,y),(x+w,y+h),(255, 128, 128),2)
                #draw net
                p1x = x + w//2
                p1y = y
                p2x = x + w//2
                p2y = y + h
                cv2.line(result, (p1x, p1y), (p2x, p2y), (0, 255, 0), 3)

                self.result_img = result

        self.rec = [x, y, w, h]
        self.mask = final_mask
        

    def ball_detection(self):

        # Creating kernel
        x, y, w, h = self.rec
        erosion_size = 5
        element = cv2.getStructuringElement(2, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))

        ball_segment = self.mask.copy()
        ball_segment = cv2.erode(ball_segment, element)

        detected_circles = cv2.HoughCircles(ball_segment, 
                    cv2.HOUGH_GRADIENT, 1, 50, param1 = 80,
                    param2 = 10, minRadius = 1, maxRadius = 50)

        c = np.array([0, 0, 0])
        ball_to_net = []
        if detected_circles is not None:
            # Convert the circle parameters a, b and r to integers.
            detected_circles = np.uint16(np.around(detected_circles))
        
            detected_circles = detected_circles[0, :]
            detected_circles = detected_circles[detected_circles[:, 2].argsort()]
            for pt in detected_circles:
                a, b, r = pt[0], pt[1], pt[2]
                ball_to_net.append(abs(a - (x + w//2)))  #calculate the length to net
                if(self.isdraw == True):  # Draw the circumference of the circle.
                    cv2.circle(self.result_img, (a, b), r // 2, (255, 255, 0), -1)
            
            ball_to_net = np.array(ball_to_net)
            c = detected_circles[ball_to_net.argsort()][0]
            #check ball inside table boundary
            if((c[0] > x and c[0] < x + w) and (c[1] > y and c[1] < y + h)):
                if(self.isdraw == True):  # Draw the ball in red
                    cv2.circle(self.result_img, (c[0], c[1]), c[2] // 2, (0, 0, 255), -1)
            else:
                c = np.array([0, 0, 0])

        self.ball_trajectory.append(c)
        if(self.isdraw == True):
            draw_trajectory(self.result_img, self.ball_trajectory)

    def scoring(self,):

        n_frames = 2 * self.fps #strat couting from nth frame and consider n frames to get the score
        n = len(self.ball_trajectory)
        rec = self.rec
    
        if(n > n_frames): #at the begining frames, dont do any action, wait until the first n frames has passed -> to get enough information
            trace = np.array(self.ball_trajectory) # you can interpolate some missing balls -> but not solve yet
            xc, yc, rc = trace[-1] #current frame ball pos

            net = rec[0] + rec[2] // 2
            decision_frames = trace[(-n_frames-1):-1] #get n frames for scoring decision
            rp = np.sum(decision_frames)

            if(rc > 0 and rp == 0):  #long pause = no ball afer n frames and has ball at the current frame
                self.reset = True         # after long pause, initialize new set

            side_array = {"OUT": 0, "R": 0, "L": 0} # couting all ball positions in decision frames and divide into 3 case: L side, R side or OUT
            for i in range(n_frames):
                x_axis = decision_frames[i][0]
                if(x_axis == 0): side_array["OUT"] += 1 #ball side is decided by correlation between ball and net
                elif(x_axis > net): side_array["R"] += 1
                else: side_array["L"] += 1


            if(self.reset == True): # if newset is on, you can decide the score,
                            # if newset is off, that means you already scored last set and the ball is OUT so you dont consider these frames
                if(side_array["L"] > n_frames / 1.2): self.score["R"] += 1; self.reset = False # If the ball stuck in L side, give a score to right side
                if(side_array["R"] > n_frames / 1.2): self.score["L"] += 1; self.reset = False # If the ball stuck in R side, give a score to left side
                if(side_array["OUT"] == n_frames - 1): # If the ball stuck in OUT side, check the final state and give the socre
                    a, b, r = decision_frames[0]
                    if(r > 0):
                        if(a < net): self.score["L"] += 1
                        else: self.score["R"] += 1
                        self.reset = False
    
        if(self.isdraw == True):
            draw_score(self.result_img, self.score)
