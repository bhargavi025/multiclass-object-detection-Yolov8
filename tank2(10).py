from ultralytics import YOLO

#Traing the custom model using the Yolo pre-trained model

model = YOLO("C:\\Users\\Bhargavi\\Documents\\yolov8n.pt")

results = model.train(data="C:\\Users\Bhargavi\Documents\data3.yaml",save=True,epochs=200)


"""
model = YOLO("C:\\Users\\Bhargavi\\OneDrive\\Documents\\yolo codes\\runs\\detect\\train6\\weights\\best.pt")

results = model.track(source="D:\\tanks.mp4",save=True,tracker="C:\\Users\\Bhargavi\\Documents\\bytetrack.yaml",conf=0.25,iou=0.3)

"""