How to run code go to the yolov7-custom:
1. Install Anaconda or other python interpeter to run the requirements.txts.
2. Install `requirements.txt` and `requirements_gpu.txt`.
3. After installation, run this command for custom object detection. Replace the `4.png` with an image of your choice or choose one of the ones which are available:

python detect.py --weights yolov7-cust.pt --conf 0.5 --img-size 640 --source 4.png --view-img --no-trace
4. Results can be found inside `runs/detect`. Afterwards, choose the highest `expi` folder.
