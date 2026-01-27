import cv2
from ultralytics import YOLO

person_model = YOLO("C:\\Users\\Bhargavi\\Documents\\yolov8n.pt")
tank_model = YOLO("C:\\Users\\Bhargavi\\OneDrive\\Documents\\yolo codes\\runs\\detect\\train6\\weights\\best.pt")

cap = cv2.VideoCapture("D:\\tanks.mp4")

save_video = True
if save_video:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    #creating videowrite to save output
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("output1_combined.avi",fourcc,fps,(width,height))

#loop
while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    
    #predict the above two models
    person = person_model.predict(frame,conf=0.4,classes=[0])[0]
    tank = tank_model.track(frame,conf=0.25,iou=0.7,persist=True,tracker="C:\\Users\\Bhargavi\\Documents\\bytetrack.yaml")[0]
    
    #draw bounding boxes using .plot()
    if person.boxes.xyxy.numel()>0:
        frame = person.plot()
    else:
        frame = frame.copy()
    
    if tank.boxes.xyxy.numel()>0: #.boxes is bounding boxes detected  .xyxy-tensor of shape[n,4](n is num of boxes)  
    #elements stored [x1y1,x2y2]   numel is [n,4] number of elements
        frame = tank.plot(img=frame,conf=False)
    
    cv2.imshow("combined",frame)
    
    #save the output video
    if save_video:
        output.write(frame)
        
    #exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
if save_video:
    output.release()
cv2.destroyAllWindows()