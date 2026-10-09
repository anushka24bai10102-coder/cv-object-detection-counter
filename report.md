
# Computer Vision Project Report

## Project Title
Computer Vision Object Detection and Counting System

## Student Details
- Name: anushka pundir
- Registration Number: 24BAI10102
- Course: Computer Vision
- University: VIT Bhopal University

## 1. Abstract

This project implements an image-based object detection and
counting system using Python and a pretrained YOLOv8 model.
The system detects objects, counts instances of each class,
saves an annotated image, and generates CSV files containing
detection details and object-count summaries.

## 2. Problem Statement

Identifying and counting objects manually in an image can
be time-consuming. This project explores how Computer Vision
can automate object detection and produce a structured
summary of the detected objects.

## 3. Objectives

- Detect common objects in an image.
- Count detected objects by class.
- Display confidence scores.
- Save bounding-box coordinates in a CSV file.
- Generate an object-count summary.
- Execute the application from the command line.

## 4. Tools and Technologies

- Python
- Ultralytics YOLOv8
- CSV module
- Command-line interface

## 5. Methodology

1. Accept an image path and confidence threshold.
2. Validate the input image.
3. Load the pretrained detection model.
4. Detect objects and obtain bounding boxes.
5. Group detections by class and count them.
6. Save the annotated image.
7. Generate individual-detection and summary CSV files.

## 6. System Workflow

Input Image
    |
    v
Input Validation
    |
    v
Load YOLOv8 Model
    |
    v
Object Detection
    |
    v
Confidence Filtering
    |
    v
Object Counting
    |
    v
Save Annotated Image and CSV Reports

## 7. Implementation

The main implementation is in main.py. Dependencies are
listed in requirements.txt, and setup instructions are
provided in README.md.

Example command:

python main.py --source test.jpg

## 8. Testing and Results

Test the program on at least three different images.

Test 1:
Input image: [Filename]
Objects detected: [Record actual results]
Observed behaviour: [Your observation]

Test 2:
Input image: [Filename]
Objects detected: [Record actual results]
Observed behaviour: [Your observation]

Test 3:
Input image: [Filename]
Confidence threshold: [Value used]
Observed behaviour: [Your observation]

Attach genuine screenshots of the terminal output and
annotated images if required by the course instructions.

## 9. Limitations

The system can miss objects or produce incorrect detections.
Its performance depends on the input image and the categories
supported by the pretrained model. A model prediction is not
a guarantee that every object has been identified correctly.

## 10. Conclusion

This project demonstrates an image-based Computer Vision
workflow that combines object detection, class-wise counting,
annotated-image generation, and CSV reporting. Testing on
different images helps illustrate the capabilities and
limitations of pretrained object detection.

## 11. Future Scope

- Real-time webcam detection.
- Video object detection and tracking.
- Testing on labelled datasets.
- Precision and recall evaluation.
- Comparison of model configurations.

## 12. References

1. Ultralytics documentation:
   https://docs.ultralytics.com/

2. YOLO prediction guide:
   https://docs.ultralytics.com/modes/predict/
