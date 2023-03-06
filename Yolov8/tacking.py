from ultralytics import YOLO

model  =  YOLO("yolov8s.pt")

ok = model.track(source="0", conf=0.25, iou = 0.7, show = True, save= True)