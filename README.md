# multiclass-object-detection-Yolov8
Armored vehicle detection using YOLOv8 trained on a custom dataset with integrated pretrained person detection for multi-class video inference.

This project implements an end-to-end object detection and tracking pipeline for detecting armored vehicles such as tanks and artillery using a custom dataset trained with YOLOv8.
A pretrained YOLO model is additionally used for person detection, enabling multi-class detection and tracking in video streams.
The system achieves high detection accuracy due to a larger custom dataset (200 images) and optimized training configuration.

Technologies used: 
1. Python  
2. Ultralytics YOLOv8    
3. OpenCV  
4. CUDA GPU Acceleration  
5. Object Tracking - ByteTrack

Dataset Details
1. Classes: Tank, Artillery
2. Annotation Format: YOLO
3. Annotation Tool: labelImg

   
