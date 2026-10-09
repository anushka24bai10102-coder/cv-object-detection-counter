
# Computer Vision Object Detection and Counting

## Project Overview

This project uses Python and a pretrained YOLOv8 model to
detect and count objects in an input image. It saves an
annotated image, individual detection details, and a CSV
summary of object counts.

## Objectives

- Detect objects in images using Computer Vision.
- Count detected objects by class.
- Display confidence scores.
- Save bounding-box coordinates in a CSV file.
- Generate an object-count summary.

## Technologies Used

- Python
- Ultralytics YOLOv8
- CSV file handling
- Command-line interface

## Project Structure

    cv-object-detection-counter/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── report.md
    ├── .gitignore
    └── outputs/

## Requirements

- Python 3.10 or newer
- Internet connection for the initial model download
- An image containing objects to detect

## Installation

### 1. Clone the repository

Replace YOUR-USERNAME with your GitHub username.

    git clone https://github.com/YOUR-USERNAME/cv-object-detection-counter.git

### 2. Open the project folder

    cd cv-object-detection-counter

### 3. Create a virtual environment

On macOS or Linux:

    python3 -m venv .venv
    source .venv/bin/activate

### 4. Install dependencies

    python -m pip install --upgrade pip
    pip install -r requirements.txt

## Running the Project

Place an image named test.jpg in the project folder.

Run:

    python main.py --source test.jpg

To change the confidence threshold:

    python main.py --source test.jpg --confidence 0.40

To change the output directory:

    python main.py --source test.jpg --output-dir results

## Output Files

- detected_result.jpg: annotated image with detected objects.
- detections.csv: individual labels, confidence scores,
  and bounding-box coordinates.
- detection_summary.csv: count and average confidence
  for each detected object class.

## Working Principle

1. Read and validate the input image.
2. Load the pretrained YOLOv8 model.
3. Detect object classes and bounding boxes.
4. Filter detections using the confidence threshold.
5. Count objects by class.
6. Save detection details and summary to CSV.
7. Save the annotated image and print results.

## Limitations

Detection results depend on image quality, object size,
lighting, and the model's training categories. The system
may miss objects or produce incorrect detections.

## Future Improvements

- Webcam-based object detection.
- Video processing.
- Evaluation using a labelled dataset.
- Comparison of detection models.

## References

Ultralytics documentation:
https://docs.ultralytics.com/

YOLO prediction guide:
https://docs.ultralytics.com/modes/predict/

