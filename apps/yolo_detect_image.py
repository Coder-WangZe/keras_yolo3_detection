import os
import numpy as np
path = os.path.abspath(__file__)
cwd = os.path.split(path)[0]
if cwd.endswith('apps'):
    os.chdir(cwd[0:-4])
    cwd = os.getcwd()
from yolo import YOLO
from PIL import Image
from timeit import default_timer as timer


def detect_image(yolo, input_image, output_image_dir, show_img=False):
    image = Image.open(input_image)

    image_name = os.path.split(input_image)[1]
    # convert jpg to png image
    if image_name.endswith(".png"):
        jpg_image = Image.new("RGB", image.size, (255, 255, 255))
        jpg_image.paste(image)
        new_img = yolo.detect_image(jpg_image)
    else:
        new_img = yolo.detect_image(image)
    if show_img:
        new_img.show()
    name = output_image_dir + image_name
    new_img.save(name)


# os.chdir('D:\\hat_mask_detection\\')
# yolo = YOLO()
# image_dir = "D:\\hat_mask_detection\\kitchen_data\\image2\\153.png"
# output_image_dir = "D:\\hat_mask_detection\\output_image\\"
# detect_image(yolo, image_dir, output_image_dir)
# yolo.close_session()

start = timer()
yolo = YOLO()
all_image_dir = 'D:\\project3\\chef_hats\\raw_image_data\\all_image\\'
output_image_dir = "D:\\project3\\chef_hats\\output_image\\output\\"
image_list = os.listdir(all_image_dir)
image_dirs = [all_image_dir + image for image in image_list]
for image_dir in image_dirs:
    detect_image(yolo, image_dir, output_image_dir)
yolo.close_session()

print("cost time: ", round((timer()-start)/60, 2))
