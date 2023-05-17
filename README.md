How to run code go to the yolov7-custom:
Install requirements.txt and requirements_gpu.txt
After installation run this command for custom object detection replace the 4.png with image of your choice or choose one of the ones which are available:
python detect.py --weights yolov7-cust.pt --conf 0.5 --img-size 640 --source 4.png --view-img --no-trace
Results can be found inside runs/detect afterwards choose the highest expi folder