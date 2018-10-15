# import the necessary packages
# -*- coding: utf-8 -*-
from __future__ import print_function #确保代码同时在Python2.7和Python3上兼容
from keras.models import Model
from keras.models import load_model
from keras import backend as k
import datetime
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import keras.preprocessing.image as kerasImage
from keras.applications.resnet50 import preprocess_input
import sys
import numpy
from keras import backend

class Evaluate():
    def __init__(self):
        self.DATASET = '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata'
        self.testimages = []
        self.features = []

    def extract_test_feature(self,dir_path, net):
        #打开文件
        f = open(
            '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/features.txt',
            'w')
        #print("写入文件的feature")
        for image_name in os.listdir(dir_path):
            if image_name == '.DS_Store':
                continue
            arr = image_name.split('_')
            # 将多个路径组合后返回（文件名字+图像名字）
            image_path = os.path.join(dir_path, image_name)
            self.testimages.append(image_path)
            # 加载图像
            img = kerasImage.load_img(image_path, target_size=(224, 224))
            # 图像预处理
            # 将一个PIL图像实例转换为一个Numpy数组。
            x = kerasImage.img_to_array(img)
            # 在第axis位置增加一个维度
            x = np.expand_dims(x, axis=0)
            # 完成数据预处理的工作，数据预处理能够提高算法的运行效果
            x = preprocess_input(x)
            # 对图像进行分类
            feature = net.predict(x)
            # 从数组的形状中删除单维度条目，即把shape中为1的维度去掉，添加到features这个list中
            self.features.append(np.squeeze(feature))
            #写入文件
            f.write('image_name:'+ image_name)
            f.write("feature:")

            for j in range(len(feature[0][0][0])):
                fe = str(feature[0][0][0][j])
                #print(fe)
                f.write(fe)
                f.write(' ')
            f.write('\n')
        f.close()

        return self.features

    def extract_query_feature(self, dir_path, net):
        # 加载图像
        # img = image.load_img(image_path, target_size=(224, 224))
        # 图像预处理
        # 将一个PIL图像实例转换为一个Numpy数组。
        img = kerasImage.load_img(dir_path, target_size=(224, 224))
        x = kerasImage.img_to_array(img)
        # 在第axis位置增加一个维度
        x = np.expand_dims(x, axis=0)
        # 完成数据预处理的工作，数据预处理能够提高算法的运行效果
        x = preprocess_input(x)
        # 对图像进行分类
        feature = net.predict(x)
        # 从数组的形状中删除单维度条目，即把shape中为1的维度去掉，添加到features这个list中
        self.features.append(np.squeeze(feature))
        # 人和相机的信息添加到infos这个list中
        # infos.append((person, camera))
        return self.features

    def extract_feature(self,dir_path, net, a):
        # 使用之前先清空里面含有的图片
        if a == 1:
            self.features = self.extract_test_feature(dir_path,net)
            # print("test_f:")
            # for i in range(len(self.features)):
            #     print(self.features[i])
        elif a == 2:
            self.features = self.extract_query_feature(dir_path,net)
        return self.features

    def query_sort(self, TEST_NUM, test_f, query_f,dir_path):
        for image_name in os.listdir(dir_path):
            if image_name == '.DS_Store':
                continue
            arr = image_name.split('_')
            # 将多个路径组合后返回（文件名字+图像名字）
            image_path = os.path.join(dir_path, image_name)
            self.testimages.append(image_path)
        query_sort_all_images = [[0 for t in range(2)] for i in range(TEST_NUM)]
        #被查询的照片
        query_feature = query_f[0]
        distances = []
        #求当前照片与查询数据集中其他照片的欧式距离
        for test_feature in test_f:
            distance = np.sqrt(np.sum(np.square(query_feature - test_feature)))
            distances.append(distance)

        #将查询数据集的照片以及对应的欧式距离存入二维数组
        for i in range(TEST_NUM):
            query_sort_all_images[i][0] = self.testimages[i]
            query_sort_all_images[i][1] = distances[i]
        # 冒泡排序对欧式距离进行排序
        for i in range(TEST_NUM - 1):
            for j in range(TEST_NUM - i - 1):
                if query_sort_all_images[j][1] > query_sort_all_images[j + 1][1]:
                    t = query_sort_all_images[j]
                    query_sort_all_images[j] = query_sort_all_images[j + 1]
                    query_sort_all_images[j + 1] = t
        #返回欧式距离小于22的
        #self.testimages = []
        return query_sort_all_images

    def image_evaluate(self,image):
        count = 107
        TEST = os.path.join(self.DATASET, 'imageEvery')
        TEST_NUM = count  # os.listdir(TEST)
        # QUERY = os.path.join(DATASET, 'imageTest')
        QUERY = image
        backend.clear_session()
        net = load_model(
            '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/duke.ckpt')
        net = Model(input=net.input, output=net.get_layer('avg_pool').output)
        #test_f = self.extract_feature(TEST, net, 1)
        query_f = self.extract_feature(QUERY, net, 2)
        #读文件
        f = open('/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/features.txt',
            'r')
        features = []
        while 1:
            #按行读取数据，这个行并不是文本中的行，因为有2048维，一行显示不完，因此按照行读取也会把2048维数据都读出来，在文本中显示好多行
            line = f.readline()
            fe = []
            if not line:
                break
            if line != '':
                line = line[30:]
                #按照空格分割，变成含有很多个str类型的元素的list
                l = line.split()
                for i in range(len(l)):
                    #将list的每一个元素str类型转换为float类型
                    a = float(l[i])
                    # list中添加这个元素
                    fe.append(a)
                #将这个list转换为array类型
                fe1 = numpy.array(fe)
                features.append(fe1)
        f.close()
        print("开始执行detect下evaluate1(image,1)函数的query_sort")
        query_sort_all_images = self.query_sort(TEST_NUM, features, query_f,TEST)
        #query_sort_all_images = self.query_sort(TEST_NUM, features, query_f, TEST)
        print("执行完detect下evaluate1(image,1)函数的query_sort")
        return query_sort_all_images

    def evaluate(self, image):
        query_sort_all_images = self.image_evaluate(image)
        return query_sort_all_images

image = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/imageQuery/0058_01.png"
qsai = Evaluate().evaluate(image)
print("sort 之后的结果。。。。。")
for i in range(len(qsai)):
    print(qsai[i])
