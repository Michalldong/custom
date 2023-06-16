import cv2
import os
import shutil






def median_filter(image_path):
    # Read the image in BGR format
    image = cv2.imread(image_path)

    # Apply Median Filter with a kernel size of 3
    filtered_image = cv2.medianBlur(image, 3)

    # Convert the filtered image back to its original color space
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

    # Create the output directory if it doesn't exist
    output_directory = 'images_enhanced/median/images/'
    os.makedirs(output_directory, exist_ok=True)
    label_directory = 'images_enhanced/median/labels/'
    os.makedirs(label_directory,exist_ok=True)

    # Extract the image name and extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image_extension = os.path.splitext(os.path.basename(image_path))[1]

    # Construct the output file path
    output_file_path = os.path.join(output_directory, image_name + image_extension)

    # Save the filtered image
    cv2.imwrite(output_file_path, filtered_image)





def histogram_equalization(image_path):
    # Read the image in BGR format
    image = cv2.imread(image_path)

    # Convert the image to YCrCb color space
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Split the YCrCb channels
    y_channel, cr_channel, cb_channel = cv2.split(ycrcb_image)

    # Equalize the Y channel
    equalized_y_channel = cv2.equalizeHist(y_channel)

    # Merge the equalized Y channel with the other channels
    equalized_ycrcb_image = cv2.merge((equalized_y_channel, cr_channel, cb_channel))

    # Convert the equalized YCrCb image back to BGR format
    equalized_image = cv2.cvtColor(equalized_ycrcb_image, cv2.COLOR_YCrCb2BGR)

    # Create the output directory if it doesn't exist
    output_directory = 'images_enhanced/histogram/images/'
    os.makedirs(output_directory, exist_ok=True)
    label_directory = 'images_enhanced/histogram/labels/'
    os.makedirs(label_directory,exist_ok=True)
    
    # Extract the image name and extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image_extension = os.path.splitext(os.path.basename(image_path))[1]

    # Construct the output file path
    output_file_path = os.path.join(output_directory, image_name + image_extension)

    # Save the equalized image
    cv2.imwrite(output_file_path, equalized_image)




def gaussian_filter(image_path):
    # Read the image in BGR format
    image = cv2.imread(image_path)

    # Apply Gaussian Filter with a kernel size of 3
    filtered_image = cv2.GaussianBlur(image, (3, 3), 0)

    # Convert the filtered image back to its original color space
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

    # Create the output directory if it doesn't exist
    output_directory = 'images_enhanced/gaussian/images/'
    os.makedirs(output_directory, exist_ok=True)
    label_directory = 'images_enhanced/gaussian/labels/'
    os.makedirs(label_directory,exist_ok=True)

    # Extract the image name and extension
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image_extension = os.path.splitext(os.path.basename(image_path))[1]

    # Construct the output file path
    output_file_path = os.path.join(output_directory, image_name + image_extension)

    # Save the filtered image
    cv2.imwrite(output_file_path, filtered_image)

# Define the source and destination directories
def destination_dir(destination_directory):
    source_directory = 'imagesTest/labels/'

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    # Get a list of all files in the source directory
    files = os.listdir(source_directory)

    # Filter the list to only include .txt files and construct the full file path
    txt_files = [os.path.join(source_directory, file) for file in files if file.endswith('.txt')]

    # Copy each .txt file to the destination directory
    for txt_file in txt_files:
        shutil.copy2(txt_file, destination_directory)


def run_all():
    directory = 'imagesTest/images/'

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Filter the list to only include .jpg files and construct the full file path
    jpg_files = [os.path.join(directory, file) for file in files if file.lower().endswith('.jpg')]

    # Print the list of .jpg files with full file paths
    for jpg in jpg_files:
        median_filter(jpg)
        histogram_equalization(jpg)
        gaussian_filter(jpg)


    destination_dir('images_enhanced/histogram/labels/')
    destination_dir('images_enhanced/median/labels/')
    destination_dir('images_enhanced/gaussian/labels/')



run_all()
