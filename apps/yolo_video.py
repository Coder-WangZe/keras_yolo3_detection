import sys
import argparse
import os
from yolo import YOLO, detect_video
from PIL import Image
path = os.path.abspath(__file__)
cwd = os.path.split(path)[0]
if cwd.endswith('apps'):
    os.chdir(cwd[0:-4])
    cwd = os.getcwd()

yolo = YOLO()
video_path = 'D:/project3/chef_hats/video/2.mp4'
detect_video(yolo, video_path)
