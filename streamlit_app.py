import torch
import numpy as np
import cv2


YOLOV_MODEL = 'best-2.02.pt'
PATH_TO_YLOLOV = 'yolov5'

class ObjectDetection:
    
    def __init__(self, path_to_photo):
        self.path_to_photo = path_to_photo
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_image_capture(self):
        return cv2.imread(self.path_to_photo)

    def load_model(self, PATH_TO_YLOLOV, YOLOV_MODEL):
        PATH_TO_YLOLOV=PATH_TO_YLOLOV
        YOLOV_MODEL=YOLOV_MODEL
        model = torch.hub.load(PATH_TO_YLOLOV, 'custom', source='local', path=YOLOV_MODEL, force_reload=True)
        return model

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def __call__(self):
        frame = self.get_image_capture()
        
        results = self.score_frame(frame)
        frame = self.plot_boxes(results, frame)
        
        cv2.imshow('YOLOv5 Detection', frame)
      
        frame.release()
        
detector = ObjectDetection(path_to_photo='all/0.jpg')
detector()
