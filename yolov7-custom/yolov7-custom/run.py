import os

###################Run valid weights with dataset unenhanced images#####################################
os.system(f'python test.py --weights  runs/train/yolov7-custom8/weights/best.pt --data unenhanced.yaml --img-size 480 --batch-size 4 --verbose')
###################Run valid weights with dataset unenhanced images#####################################

###################Run valid weights with dataset histogram equilization images#####################################
os.system(f'python test.py --weights  runs/train/yolov7-custom8/weights/best.pt --data histogram.yaml --img-size 480 --batch-size 4 --verbose')
###################Run valid weights with dataset histogram equilization images#####################################

# ###################Run valid weights with dataset median filter images#####################################
os.system(f'python test.py --weights  runs/train/yolov7-custom8/weights/best.pt --data median.yaml --img-size 480 --batch-size 4 --verbose')
# ###################Run valid weights with dataset median filter images#####################################

# ###################Run valid weights with dataset gaussian filter images#####################################
os.system(f'python test.py --weights  runs/train/yolov7-custom8/weights/best.pt --data gaussian.yaml --img-size 480 --batch-size 4 --verbose')
###################Run valid weights with dataset gaussian filter images#####################################

