from ultralytics import YOLO
from ultralytics.engine.results import Results

# Load the YOLO model
model = YOLO('yolov8n.pt')

# Train the model
model.train(
    data='data.yaml',
    epochs=30,
    imgsz=640,
    batch=16,
    workers=4,
    save_dir='U:\\YOLO\\runs\\train3'
)
