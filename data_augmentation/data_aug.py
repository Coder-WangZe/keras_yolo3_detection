from data_augmentation.xml_helper import *
from data_augmentation.DataAugmentForObjectDetection import *
import cv2
import os


def data_aug_sinlge(augmenter, xml_path, out_image_path, out_xml_path, rotate, hori_flip, add_noise):
    # 读取原图片路径和box
    image_path, bbox = parse_xml(xml_path)
    image_name = os.path.split(image_path)[1]
    # 读取源图片
    image = cv2.imread(image_path)
    if rotate:
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

    if hori_flip:
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

    if add_noise:
        # augment 2: flip
        aug_class = "add_noise"
        auged_image = augmenter._addNoise(image)
        auged_bbox = bbox
        # 输出图片的路径
        auged_image_path = out_image_path + "/" + image_name[:-4] + aug_class + image_name[-4:]
        cv2.imwrite(auged_image_path, auged_image)
        img_size = (120, 120, 3)
        generate_xml(auged_image_path, auged_bbox, img_size, out_xml_path)
        # show_pic(auged_image, auged_bbox)


def data_aug(augmenter, xml_path, out_image_path, out_xml_path, rotate, hori_flip, add_noise):
    # out_xml_path = xml_path
    out_image_path = os.path.abspath(out_image_path)
    all_xml_path = [xml_path + xml_name for xml_name in os.listdir(xml_path) if xml_name.endswith(".xml")]
    for i, single_xml_path in enumerate(all_xml_path):
        data_aug_sinlge(augmenter, single_xml_path, out_image_path, out_xml_path, rotate, hori_flip, add_noise)
    print("data augmentation successfully !")


if __name__ == "main":
    xml_path = os.path.dirname(__file__) + "/data_xml/"
    out_image_path = os.path.dirname(__file__) + "/augmented_data/image"
    out_xml_path = os.path.dirname(__file__) + "/augmented_data/annotations"

    augmenter = DataAugmentForObjectDetection()

    data_aug(augmenter, xml_path, out_image_path, out_xml_path, rotate=True, hori_flip=True, add_noise=True)



