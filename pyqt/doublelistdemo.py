
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import os
import sys
import numpy as np
import tensorflow as tf
import pickle
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.models import Model
from keras.backend.tensorflow_backend import set_session
from keras.models import load_model
from PIL import Image


queryimages = []
testimages = []
DATASET = '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/data'
TEST = os.path.join(DATASET, '1')
QUERY = os.path.join(DATASET, '2')
TEST_NUM = 11
QUERY_NUM = 11
distance = 0
net = load_model('/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/duke.ckpt')
net = Model(input=net.input, output=net.get_layer('avg_pool').output)


def extract_feature(dir_path, net):
  features = []
  infos = []
  num = 0
  for image_name in os.listdir(dir_path):
    #使用 '_'分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
    arr = image_name.split('_')
    person = int(arr[0])
    camera = int(arr[1][1]) #为什么是arr[1][1]呢
    #将多个路径组合后返回（文件名字+图像名字）
    image_path = os.path.join(dir_path, image_name)

    if dir_path == TEST:
      testimages.append(image_path)

    elif dir_path == QUERY:
       queryimages.append(image_path)

    #加载图像
    img = image.load_img(image_path, target_size=(224, 224))

    #图像预处理
    #将一个PIL图像实例转换为一个Numpy数组。
    x = image.img_to_array(img)
    #在第axis位置增加一个维度
    x = np.expand_dims(x, axis=0)
    #完成数据预处理的工作，数据预处理能够提高算法的运行效果
    x = preprocess_input(x)

    #对图像进行分类
    feature = net.predict(x)

    #从数组的形状中删除单维度条目，即把shape中为1的维度去掉，添加到features这个list中
    features.append(np.squeeze(feature))
    #人和相机的信息添加到infos这个list中
    infos.append((person, camera))

  # print("testimages")
  # print(testimages)
  # print("haha")
  return features, infos

extract_feature(TEST, net)
extract_feature(QUERY, net)

TEST_NUM = 11
f1 = open("/Users/huan/code/pythondemo/test_f.txt",'rb')
test_f = pickle.load(f1)

f2 = open("/Users/huan/code/pythondemo/query_f.txt",'rb')
query_f = pickle.load(f2)

#定义一个二维数组
A = [[0 for t in range(2)]for i in range(TEST_NUM)]
#query一张照片，每一个test照片以及与query的distance存在一个二维list的元素里

for query_feature in query_f:
  distances = []
  for test_feature in test_f:
    distance = np.sqrt(np.sum(np.square(query_feature - test_feature)))
    distances.append(distance)
  for i in range(TEST_NUM):
      print("i的值" + str(i))
      A[i][0] = testimages[i]
      #print("a[i][0]"+A[i][0]+"  testimage" + testimages[i] )
      A[i][1] = distances[i]
      #print(A[i][0] + " " + str(A[i][1]) + "\n")
  #冒泡排序对欧式距离进行排序
  for i in range(TEST_NUM - 1):
      count = 0
      for j in range(TEST_NUM - i - 1):
          if A[j][1] > A[j + 1][1]:
              t = A[j][1]
              A[j][1] = A[j + 1][1]
              A[j + 1][1]    = t

  for i in range(TEST_NUM):
      for j in range(2):
          print(A[i][j])
      print("\n")


