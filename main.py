
import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path

from ultralytics import YOLO


def detect_objects(image_path, confidence, output_dir):
    image = Path(image_path)
    output = Path(output_dir)

    # Check that the input image exists.
    if not image.is_file():
        raise FileNotFoundError(f"Input image not found: {image}")

    output.mkdir(parents=True, exist_ok=True)

    # Load the pretrained YOLOv8 nano model.
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")

    # Detect objects in the input image.
    print("Detecting objects...")
    results = model.predict(
        source=str(image),
        conf=confidence,
        verbose=False
    )

    result = results[0]

    # Save the image with bounding boxes and labels.
    image_output = output / "detected_result.jpg"
    result.save(filename=str(image_output))

    # Collect detection information.
    detections = []
    counts = Counter()
    confidence_values = defaultdict(list)

    if result.boxes is not None:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            score = float(box.conf[0])

            counts[label] += 1
            confidence_values[label].append(score)

            detections.append({
                "image": image.name,
                "object": label,
                "confidence": round(score, 4),
                "x_min": round(float(box.xyxy[0][0]), 2),
                "y_min": round(float(box.xyxy[0][1]), 2),
                "x_max": round(float(box.xyxy[0][2]), 2),
                "y_max": round(float(box.xyxy[0][3]), 2)
            })

    # Save details of every detection to a CSV file.
    details_file = output / "detections.csv"
    detail_fields = [
        "image", "object", "confidence",
        "x_min", "y_min", "x_max", "y_max"
    ]

    with details_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=detail_fields)
        writer.writeheader()
        writer.writerows(detections)

    # Save the number of objects of each class.
    summary_file = output / "detection_summary.csv"

    with summary_file.open("w", newline="", encoding="utf-8") as file:
        fields = ["object", "count", "average_confidence"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for label, count in sorted(counts.items()):
            average = sum(confidence_values[label]) / count
            writer.writerow({
                "object": label,
                "count": count,
                "average_confidence": round(average, 4)
            })

    # Display results in the terminal.
    print("\n--- Detection Results ---")
    print(f"Input image: {image.name}")
    print(f"Total objects detected: {len(detections)}")

    if counts:
        for label, count in sorted(counts.items()):
            print(f"{label}: {count}")
    else:
        print("No objects detected at this confidence threshold.")

    print(f"\nAnnotated image: {image_output}")
    print(f"Detection details: {details_file}")
    print(f"Object count summary: {summary_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Computer Vision Object Detection and Counting"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--confidence",
        type=float,
        default=0.25,
        help="Minimum confidence threshold from 0 to 1"
    )

    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for saved results"
    )

    args = parser.parse_args()

    if not 0 <= args.confidence <= 1:
        parser.error("Confidence must be between 0 and 1.")

    try:
        detect_objects(
            args.source,
            args.confidence,
            args.output_dir
        )
    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
