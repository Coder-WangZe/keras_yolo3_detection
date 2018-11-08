# -*- coding=utf-8 -*-
import xml.etree.ElementTree as ET
import os


"""xml文件中的image path信息要与不同机器的image path对应，该脚本进行xml中 path的转换，
输入为原始xml文件的路径，当前机器对应image data的路径，以及输出xml文件的路径，
注意：xml文件的数量应与图片数量一致"""


def convert_image_path(xml_path, image_path):

    output_path = xml_path
    # xml_path = "./data_augmentation/hat_xml/"
    xml_path = os.path.abspath(xml_path)
    xmls_ls = [xml_path + "\\" + xml_name for xml_name in os.listdir(xml_path) if xml_name.endswith(".xml")]
    img_path = os.path.abspath(image_path)
    img_ls = [img_path + "\\" + image_name for image_name in os.listdir(img_path)
              if image_name.endswith(".jpg") or image_name.endswith(".png")]
    if len(img_ls) != len(xmls_ls):
        print("图片数量与xml文件的数量不匹配！")
    output_path = os.path.abspath(output_path)
    for i, xml in enumerate(xmls_ls):
        tree = ET.parse(xml)
        root = tree.getroot()
        path = root.findall("path")
        path[0].text = img_ls[i]
        tree.write(output_path + "\\" + os.path.split(xml)[1])
    print(" convert successfully ! \n total xml nums: %d" % (i+1))


if __name__ == "main":
    xml_path = "./hat_xml/"
    image_path = "./raw_image/"
    output_path = "./new_hat_xmls/"
    convert_image_path(xml_path, image_path, output_path)
