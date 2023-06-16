<<<<<<< HEAD
# How to Run the Code

1. Install Anaconda
2. Navigate to the `yolov7-custom` folder in anaconda.
3. Install the required dependencies:
    1. Run the following command to install the dependencies from `requirements.txt`:
        ```
        pip install -r requirements.txt
        ```
    2. If you have an Nvidia GPU and want to enable GPU support, also install the dependencies from `requirements_gpu.txt`:
        ```
        pip install -r requirements_gpu.txt
        ```

4. Train the model on a specific task (requires Nvidia GPU for faster training also there is already trained models inside):
    1. Download dataset from https://universe.roboflow.com/footballevents/allfootballevents
    2. Unzip the file and put  inside the data folder the following folder test, train, valid folder.
    3. Open Anaconda Prompt or a terminal.
    4. Navigate to the `yolov7-custom` folder if you haven't already.
    5. Run the following command to train the model:
        ```
        python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 480 480 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7_custom.yaml --name yolov7-custom --weights yolov7.pt
        ```
    > Note: Training without an Nvidia GPU will take a significantly longer time.

5. Perform image enhancement:
    * Run the `image_enhancement.py` script inside the `yolov7-custom` folder
    * This will create the `images_enhanced` folder and populate it with enhanced images from the `imagesTest` folder, if it doesn't exist already.

6. Obtain metrics of the tested images:
    * Run the `run.py` script inside the `yolov7-custom` folder.
    * This will generate the metrics for the tested images.
    * Results are saved within the runs/test/ where you need to choose the highest exp folder.
    > Note: If you want to test your own model on the images modify the ```runs/train/yolov7-custom8/weights/best.pt``` and change the number in custom8 to your own custom model.
    
    > Note: Having an Nvidia GPU will speed up the process.


=======
How to run code go to the yolov7-custom:
1. Install Anaconda or other python interpeter to run the requirements.txts.
2. Install `requirements.txt` and `requirements_gpu.txt`.
3. After installation, run this command for custom object detection. Replace the `4.png` with an image of your choice or choose one of the ones which are available: python detect.py --weights yolov7-cust.pt --conf 0.5 --img-size 640 --source 4.png --view-img --no-trace
4. Results can be found inside `runs/detect`. 
>>>>>>> cb0f0b528a8c9101559544aec1dfac64a79ad667
