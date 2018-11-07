# keras_yolo3_detection
yolov3;
keras;
object detection;
data augmentation


将原始的xml文件放在data_augmentation\data_xml\目录下，xml文件中的路径要与image对应

1 运行data_augs.py,得到增强后的数据image和xml文件 xml文件输出在目录data_augmentation\annotations\下 然后将原始的xml文件复制在该目录下。

2 运行data_annotations.py 该脚本中的class要包括标注时添加的所有种类如“hat”，“nohat” 运行得到train_list和test_list的txt文件

3 运行train.py训练
