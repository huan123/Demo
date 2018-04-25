#########冒泡排序######
TEST_NUM = 6
A = [TEST_NUM]
A = [9,3,5,8,7,1]
for i in range( TEST_NUM - 1):
    count = 0
    for j in range(TEST_NUM - i - 1):
        if A[j] > A[j + 1]:
            t = A[j]
            A[j] = A[j + 1]
            A[j + 1] = t
    # if count == 0:
    #     break
print(A)


