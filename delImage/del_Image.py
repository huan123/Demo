import os
paths = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/testimages/"
for im_name in os.listdir(paths):
    path_file = os.path.join(paths, im_name)
    os.remove(path_file)