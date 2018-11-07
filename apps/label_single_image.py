from PIL import Image
import os
import shutil
import cv2


def label_single_img(input_image_dir, output_dir):
    image_list = os.listdir(input_image_dir)
    image_dirs = [input_image_dir + "\\" + image for image in image_list]
    hat_path = output_dir + "/hat"
    nohat_path = output_dir + "/no_hat"
    others_path = output_dir + "/others"
    if os.path.exists(others_path):
        shutil.rmtree(others_path)
        os.mkdir(others_path)
        print("others_path overwritten !")
    else:
        os.mkdir(others_path)
    if os.path.exists(hat_path):
        shutil.rmtree(hat_path)
        os.mkdir(hat_path)
        print("hat_path overwritten !")
    else:
        os.mkdir(hat_path)
    if os.path.exists(nohat_path):
        shutil.rmtree(nohat_path)
        os.mkdir(nohat_path)
        print("nohat_path overwritten !")
    else:
        os.mkdir(nohat_path)
    for i, img_dir in enumerate(image_dirs):
        print("the %dth image procssing !" % i)
        img = cv2.imread(img_dir)
        cv2.resizeWindow("image", 6400, 4800)
        cv2.imshow("image", img)
        cv2.waitKey(30)
        key = input("Please input your judgement: ")
        if key == "y":
            cv2.imwrite(hat_path + "/" + os.path.split(img_dir)[1], img)
        elif key == "u":
            cv2.imwrite(others_path + "/" + os.path.split(img_dir)[1], img)
        else:
            cv2.imwrite(nohat_path + "/" + os.path.split(img_dir)[1], img)
        cv2.destroyWindow("image")

    print("all image labeled ! ")


if __name__ == "__main__":
    input_image_dir = "D:\\project3\\chef_hats\\output_image\\cropped\\"
    output_dir = "D:\\project3\\chef_hats\\hat_classfier\\train_image"
    label_single_img(input_image_dir, output_dir)


