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


def crop_image(yolo, input_image, output_image_dir, show_img=False):
    image = Image.open(input_image)

    image_name = os.path.split(input_image)[1]
    cropped_imgs = yolo.crop_image(image)

    for i, img in enumerate(cropped_imgs):
        name = image_name[0: -4]
        import cv2
        image = Image.fromarray(img)
        if show_img:
            image.show()
        # cv2.imwrite(output_image_dir + name + '_' + str(i) + '.jpg', img)
        path = output_image_dir + "\\" +name + '_' + str(i) + image_name[-4:]
        image.save(path)


start = timer()
yolo = YOLO()
all_image_dir = 'D:\\project3\\chef_hats\\raw_image_data\\all_image\\'
output_image_dir = 'D:\\project3\\chef_hats\\output_image\\cropped'
if os.path.exists(output_image_dir):
    if os.listdir(output_image_dir):
        # import shutil
        # shutil.rmtree(output_image_dir)
        os.removedirs(output_image_dir)
        os.mkdir(output_image_dir)
else:
    os.mkdir(output_image_dir)

image_list = os.listdir(all_image_dir)
image_dirs = [all_image_dir + image for image in image_list]
for image_dir in image_dirs:
    crop_image(yolo, image_dir, output_image_dir)
yolo.close_session()

print("cost time: ", round((timer()-start)/60, 2))
