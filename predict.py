from ultralytics import YOLO

# Load a model
model = YOLO("best_aug.pt")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

model.predict(source="13.jpg", show = True , save = True)
