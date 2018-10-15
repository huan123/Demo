

#写入文件
fo = open("/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/features.doc", "w")
s = [1,3,5,8,2,29]
name = "iiiii"
for i in range(10):
    fo.write(name)
    for j in range(len(s)):
        fo.write(str(s[j]))
    fo.write('\n')
fo.close()

#从文件中读取
fo = open("/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/baseline/features.doc", "r")
#str = fo.read()
list = []
print("读取的字符串：")
while 1:
    line = fo.readline()
    if not line:
        break
    list.append(line[5:])
    print(line[5:])
fo.close()

