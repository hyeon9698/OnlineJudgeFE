import cv2
import numpy as np
 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.

 

while(True):
  ret, frame = cap.read()
 
  if ret == True: 
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()