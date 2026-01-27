from ultralytics import YOLO

#Traing the custom model using the Yolo pre-trained model

model = YOLO("yolov8n.pt")

results = model.train(data="data3.yaml",save=True,epochs=200)


"""
model = YOLO("runs\\detect\\train\\weights\\best.pt")

results = model.track(source="D:\\tanks.mp4",save=True,tracker="bytetrack.yaml",conf=0.25,iou=0.3)


"""
