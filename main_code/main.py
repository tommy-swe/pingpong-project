## Author
## Date

## Main script for run code


from LED_control import RGBLEDcontroller, DigitLEDcontrolller
import time
import os
import cv2
from Alg import PingPongAlg
import argparse


COLOR = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]

# def main():
#     controller = RGBLEDcontroller()
#     controller.setup()
#     try:
#         while True:
#             for color in COLOR:
#                 controller.setColor(color)
#                 time.sleep(0.5)
#     except KeyboardInterrupt:
#         controller.stop()

# def main():

#     controller = DigitLEDcontrolller(clk=3, dio=2)
#     try:
#         while True:
#             for (num1, num2) in [(0, 1), (1, 1), (2, 1), (2, 2)]:
#                 print(num1, num2)
#                 controller.setNumber(num1, num2)
#                 time.sleep(0.5)
#     except KeyboardInterrupt:
#         controller.reset()

# def main():
#     controller_LED = RGBLEDcontroller()
#     controller_LED.setup()
#     controller_Digit = DigitLEDcontrolller(clk=3, dio=2)

#     for video in (os.listdir("test")):

#         #start recording:
#         controller_LED.setColor(COLOR[0])

#         cap = cv2.VideoCapture(os.path.join('test', video))
#         fps = int(cap.get(cv2.CAP_PROP_FPS))
#         print("Video name: ", video)
#         print("Frame rate: ", fps, "FPS")

#         score_board = PingPongAlg(fps = fps, isshow=False, isdraw=False)

#         try:
#             while(cap.isOpened()):
#                 ret, frame = cap.read()

#                 # table detection
#                 score_board.table_detection(frame=frame)
#                 # ball detection
#                 score_board.ball_detection()
                
#                 score_board.scoring()
#                 l_score, r_score = score_board.score["L"], score_board.score["R"]
#                 print(l_score, r_score)
#                 controller_Digit.setNumber(l_score, r_score)

#                 if(score_board.isshow == True):
#                     cv2.imshow('contours',  score_board.result_img)
#                     # cv2.imshow('frame', score_board.curent_frame)
#                     cv2.waitKey(5)

#                 if 0xFF == ord('q'):
#                     break
#         except:
#             cap.release()
#             cv2.destroyAllWindows()
#             controller_LED.stop()
#             controller_Digit.reset()

#         # finally:
#         #     cap.release()
#         #     cv2.destroyAllWindows()
#         #     controller_LED.stop()
#         #     controller_Digit.reset()

## prarameters set later ----> remain

def main(args):

    controller_LED = RGBLEDcontroller()
    controller_LED.setup()
    controller_Digit = DigitLEDcontrolller(clk=3, dio=2)

    while(True):
        
        cam = cv2.VideoCapture(0)

        if (cam.isOpened() == False): 
            print("Error reading video file")
            controller_LED.setColor(COLOR[1])
            time.sleep(1)
            controller_LED.stop()
            controller_Digit.reset()
            break

        else:
            #start recording:
            st_time = time.time()
            print("new_recording")
            controller_LED.setColor(COLOR[0])
            fps = int(cam.get(cv2.CAP_PROP_FPS))
            print("Frame rate: ", fps, "FPS")
            score_board = PingPongAlg(fps = 10, isshow=args.is_showing, isdraw=args.is_drawing, issave=args.is_saving)

            if(score_board.issave == True):
                size = score_board.base_size
                fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
                # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                output = cv2.VideoWriter(str(int(st_time)) + ".avi", fourcc, fps, size)

          
            while(True):
                ret, frame = cam.read()

                if(int(time.time() - st_time) > 1 * args.set_time): #new record after n seconds
                    break
                
                try:
                    if(ret == True):
                        
                        # table detection
                        score_board.table_detection(frame=frame)
                        # ball detection
                        score_board.ball_detection()
                        #ball scoring
                        score_board.scoring()
                        l_score, r_score = score_board.score["L"], score_board.score["R"]
                        # print(l_score, r_score)
                        controller_Digit.setNumber(l_score, r_score)

                        if(score_board.isshow == True):
                            cv2.imshow('contours',  score_board.result_img)
                            # cv2.imshow('frame', score_board.curent_frame)
                            # cv2.waitKey(1)

                        # cv2.imshow('frame', frame)

                        if cv2.waitKey(1) & 0xFF == ord('s'):
                            break
                        
                        if(score_board.issave == True):
                            output.write(score_board.result_img)
                    else:
                        break
                except:
                    break

            cam.release()
            cv2.destroyAllWindows()
            # controller_LED.stop()
            controller_Digit.reset()

        print("stop")
        controller_LED.setColor(COLOR[2])
        controller_Digit.reset()
        time.sleep(args.stop_time)
        


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Hyper parameters.')
    parser.add_argument('--stop_time', metavar='N', type=int, nargs='+', required=True,
                    help='n seconds that stop recording', default=20)
    parser.add_argument('--set_time', metavar='N', type=int, nargs='+', required=True,
                    help='n seconds for a playing set', default=60)
    parser.add_argument('--is_showing', type=bool, default=True, required=True,
                    help='showing the frame')
    parser.add_argument('--is_drawing', type=bool, default=True, required=True,
                    help='drawing the frame')
    parser.add_argument('--is_saving', type=bool, default=True, required=True,
                    help='saving the frame')


    args = parser.parse_args()
    main(args)





