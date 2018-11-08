import os
from data_augmentation.convert_xml_path import *
from data_augmentation.data_aug import *
from data_augmentation.data_annotations import *


path = os.path.abspath(__file__)
cwd = os.path.split(path)[0]
if cwd.endswith('apps'):
    os.chdir(cwd[0:-4])
    cwd = os.getcwd()

"""
三步：
1 转换xml文件中的原始图像路径，覆盖原来的xml文件
2 aug image， 若未指定out xml与image的路径，则增强后的xml和image输出到原文件夹
3 convert to train list txt，将增强后的数据按比例划分为训练集和测试集并输出为train_list_txt文件
"""
# raw xml and image path
xml_path = './data_augmentation/hat_xml/'
image_path = './data_augmentation/raw_image/'
# augmented image path,auged xml path == raw xml path
auged_image_path = './data_augmentation/auged_image/'
# class name and output train list txt(each line in the txt includes the image path and box information)
classes = ["hat", "no_hat"]
output_file_dir = './'

convert_image_path(xml_path, image_path)  # 转换xml文件中的原始图像路径
augmenter = DataAugmentForObjectDetection(max_rotation_angle=5)  # 设定增强类的参数如最大旋转角度
data_aug(augmenter, xml_path, out_image_path=auged_image_path, out_xml_path=xml_path,
         rotate=True, hori_flip=True, add_noise=True)
conver_to_train_list_txt(xml_path, classes, output_file_dir, train_split=0.8)



