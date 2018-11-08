Object detection with yolov3 in keras.

Include： 
 labeling; 
 data augmentation; 
 training and testing with images and video.

一 Data augmentation for object detection：

    将标注好的xml文件放在data_augmentation\hat_xml\目录下,

    原始的image data放在data_augmentation\raw_image\目录下

    运行apps目录下data_preprocess.py,得到增强后的数据image和xml文件

    说明：

        xml文件默认输出在目录data_augmentation\hat_xml\下

        image默认输出在目录data_augmentation\auged_image\下

        data_preprocess.py三步：

        1 translate the image path of raw xml file, 覆盖原来的xml文件

        2 Image data augmentation,若未指定xml的路径,则增强后的xml输出到原文件夹

        3 convert to train list txt,将增强后的数据按比例划分为训练集和测试集并输出为train_list_txt文件

          train list txt(each line in the txt includes the image path and box information)
          
        数据增强包括旋转,水平翻转,添加噪声，改变亮度,剪裁平移等.

二 Training

     运行train.py训练
      先冻结前185层训练50个epoch,再全部解除冻结进行训练。
  
三 Test：

      设置好路径,运行 ：
      apps/yolo_detect_image;
      yolo_video
