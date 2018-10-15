# -*- coding: utf-8 -*-
import time
import datetime
def t():

    # t0 = time.clock()
    # for i in range(100):
    #     t = i + 10
    # t1 = time.clock()
    # print(str(t1-t0))

    start = time.time()
    for i in range(1000):
        t = i + 10
    stop = time.time()
    print("stop-start:")
    print(str(stop-start))


    starttime = datetime.datetime.now()
    for i in range(1000000):
        t = i + 10
    endtime = datetime.datetime.now()
    print("endtime - starttime: " + str(endtime - starttime))


t()