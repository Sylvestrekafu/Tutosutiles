from ultralytics import YOLO

model  = YOLO("yolov8s.pt")

ok = model.track(source="https://www.youtube.com/watch?v=Lc8ldWNlyEE&t=819s" , save = True, show = True, conf=0.25 , iou = 0.7)