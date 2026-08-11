import cv2
import tensorflow as tf
import numpy as np

model = tf.saved_model.load('model/ssd_mobilenet_v2_fpnlite_320x320/saved_model')
category_index = {1: 'person'}

def detect_objects():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        input_tensor = tf.convert_to_tensor([frame])
        detections = model(input_tensor)

        boxes = detections['detection_boxes'][0].numpy()
        scores = detections['detection_scores'][0].numpy()
        classes = detections['detection_classes'][0].numpy().astype(int)

        for i in range(len(scores)):
            if scores[i] > 0.5 and classes[i] in category_index:
                # Add bounding boxes
                pass  # Optional if just streaming

        _, jpeg = cv2.imencode('.jpg', frame)
        yield jpeg.tobytes()

    cap.release()