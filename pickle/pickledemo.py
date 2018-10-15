
###############将二维数组整体写入文件，读取文件中的内容#############
import  pickle

a = [[1,2],[2,3]]
#写入文件
f1 = open("/Users/huan/code/pythondemo/test.txt","wb")
pickle.dump(a,f1)
f1.close()
#从文件中读取数据
f2 = open("/Users/huan/code/pythondemo/test.txt",'rb')
test_f = pickle.load(f2)
print(test_f)
f2.close()

