import cv2
#Capture video from webcam
vid_capture_L = cv2.VideoCapture(0)
vid_capture_R = cv2.VideoCapture(1)

#vid_cod = cv2.VideoWriter_fourcc(*'XVID')
#output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640,480))
while(True):
     # Capture each frame of webcam video
     retL, frame_L= vid_capture_L.read()
     retR, frame_R= vid_capture_R.read()
     cv2.imshow("My cam video L", frame_L)
     cv2.imshow("My cam video R", frame_R)
     
     #output.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break
# close the already opened camera

vid_capture_L.release()
vid_capture_R.release()

# close the already opened file
#output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()