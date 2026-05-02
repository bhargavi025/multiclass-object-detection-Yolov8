# Armored Vehicle Detection and Tracking using YOLOv8

## Overview
This project implements a real-time multi-class object detection and tracking pipeline for identifying armored vehicles (tanks, artillery) and humans in video streams.

The system combines a custom-trained YOLOv8 model for military vehicle detection with a pretrained YOLO model for person detection, enabling a unified perception pipeline for surveillance and defense applications.

---

## Problem Statement
Detection of armored vehicles in real-world environments is critical for surveillance, defense systems, and autonomous reconnaissance. However, such objects are underrepresented in standard datasets.

This project addresses this by training a custom model specifically for armored vehicle detection and integrating it into a real-time inference system.

---

## Methodology

### Detection Pipeline
- Custom YOLOv8 model trained on armored vehicle dataset
- Pretrained YOLOv8 model for person detection
- Combined multi-class inference

### Tracking
- ByteTrack algorithm for real-time object tracking
- Maintains object identities across frames

### System Flow
1. Input video stream
2. Object detection (YOLOv8)
3. Multi-class fusion (vehicle + person)
4. Tracking using ByteTrack
5. Output annotated video

---

## Dataset
- Classes: Tank, Artillery
- Total Images: 200
- Annotation Format: YOLO
- Annotation Tool: labelImg

---

## Results

### Sample Outputs
(Add your images here)

### Performance
- Real-time inference enabled (GPU accelerated)
- Model: YOLOv8 (custom-trained + pretrained)
- Tracking: ByteTrack

---

## Technologies Used
- Python
- Ultralytics YOLOv8
- OpenCV
- CUDA (GPU acceleration)
- ByteTrack

---

## Applications
- Defense surveillance systems
- Autonomous military robots
- Threat detection and monitoring
- Computer vision-based reconnaissance

---

## Future Work
- Integrate with ROS2 for robotic deployment
- Improve dataset size and diversity
- Add thermal image detection
- Deploy on edge devices (Jetson Nano / Raspberry Pi)

---
