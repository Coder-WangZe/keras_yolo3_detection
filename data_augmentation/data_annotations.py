import xml.etree.ElementTree as ET
import os


def convert_annotation(annotation_path, image_id, list_file, classes):
    in_file = open(annotation_path + '%s.xml' % image_id)
    tree = ET.parse(in_file)
    root = tree.getroot()
    image_path = root.findall("path")[0].text
    list_file.write('%s' % image_path)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
    list_file.write('\n')


def conver_to_train_list_txt(annotation_path, classes, output_file_dir, train_split=0.8):
    if output_file_dir == "":
        output_file_dir = 'D:\\project3\\chef_hats\\'
    xml_names = os.listdir(annotation_path)
    image_ids = [xml_name[0:-4] for xml_name in xml_names if xml_name.endswith(".xml")]
    train_data_nums = int(train_split * len(image_ids))
    list_file = open(output_file_dir + 'train_list.txt', 'w')
    list_file_test = open(output_file_dir + 'test_list.txt', 'w')
    for i, image_id in enumerate(image_ids):
        if i < train_data_nums:
            convert_annotation(annotation_path, image_id, list_file, classes)
        else:
            convert_annotation(annotation_path, image_id, list_file_test, classes)
    list_file.close()
    print("convert to the trainlist txt secessfully! ")
    print("train_nums: %d " % train_data_nums)
    print("test_nums: %d " % (len(image_ids) - train_data_nums))


"""xml_file_path为标注后的XML文件路径，classes（str list）应添加所有的class name
output_txtfile_dir为输出的trainlist文件的路径，该文件包含了image的路径的bbox信息。"""
if __name__ == "main":
    xml_file_path = 'D:\\project3\\chef_hats\\annotations(hat)\\'
    classes = ["hat", "no_hat"]  # 应添加所有的class name
    train_test_list_txt__dir = 'D:\\project3\\chef_hats\\'
    conver_to_train_list_txt(xml_file_path, classes, train_test_list_txt__dir)

