from data_augmentation.xml_helper import *
from data_augmentation.DataAugmentForObejctDetection import *
import cv2
import os
path = os.path.abspath(__file__)
cwd = os.path.split(path)[0]
if cwd.endswith('apps'):
    os.chdir(cwd[0:-4])
    cwd = os.getcwd()


def data_aug_sinlge(augmenter, xml_path, out_image_path, out_xml_path):
    # 读取原图片路径和box
    image_path, bbox = parse_xml(xml_path)
    image_name = os.path.split(image_path)[1]
    # 读取源图片
    image = cv2.imread(image_path)
    # augment 1: rotate
    aug_class = "rotate"
    auged_image, auged_bbox = augmenter._rotate_img_bbox(image, bbox)
    # auged_image, auged_bbox = augmenter.dataAugment(image, bbox)
    #输出图片的路径
    auged_image_path = out_image_path + "/" + image_name[:-4] + aug_class + image_name[-4:]
    cv2.imwrite(auged_image_path, auged_image)
    img_size = (120, 120, 3)
    for i, box in enumerate(bbox):
        class_name = box[-1]
        auged_bbox[i].append(class_name)

    generate_xml(auged_image_path, auged_bbox, img_size, out_xml_path)

    # show_pic(auged_image, auged_bbox)

    # augment 2: flip
    aug_class = "horizontal_flip"
    auged_image, auged_bbox = augmenter._filp_pic_bboxes(image, bbox)
    # auged_image, auged_bbox = augmenter.dataAugment(image, bbox)
    # 输出图片的路径
    auged_image_path = out_image_path + "/" + image_name[:-4] + aug_class + image_name[-4:]
    cv2.imwrite(auged_image_path, auged_image)
    img_size = (120, 120, 3)
    for i, box in enumerate(bbox):
        class_name = box[-1]
        auged_bbox[i].append(class_name)
    generate_xml(auged_image_path, auged_bbox, img_size, out_xml_path)

    # show_pic(auged_image, auged_bbox)


def data_aug(augmenter, xml_path, out_image_path, out_xml_path):
    all_xml_path = [xml_path + xml_name for xml_name in os.listdir(xml_path)]
    for i, single_xml_path in enumerate(all_xml_path):
        data_aug_sinlge(augmenter, single_xml_path, out_image_path, out_xml_path)


xml_path = cwd + "/data_augmentation/data_xml/"
out_image_path = cwd + "/data_augmentation/image"
out_xml_path = cwd + "/data_augmentation/annotations"

augmenter = DataAugmentForObjectDetection(rotation_rate=0.2, max_rotation_angle=2,
                                          crop_rate=0.2, shift_rate=0.2, change_light_rate=0.2,
                                          add_noise_rate=0.1, flip_rate=0.2,
                                          cutout_rate=0.2, cut_out_length=20, cut_out_holes=1, cut_out_threshold=0.3)

# if __name__ == "main":
data_aug(augmenter, xml_path, out_image_path, out_xml_path)





