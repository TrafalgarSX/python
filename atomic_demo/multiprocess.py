
import os
import time
import random
from multiprocessing import Process, Queue

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def multi_process(lambda_arg):
    print('Process (%s) start...' % os.getpid())
    lambda_arg('text.txt')

    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process will start.')
    # insert list 
    p_list = []
    for i in range(5):
        p = Process(target=long_time_task, args=(i,))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

def sequential():
    for i in range(5):
        long_time_task(i)

def read_file(file_name):
    with open(file_name, 'r') as f:
        print(f.read())

if __name__ == '__main__':
    # calculate time cost
    start = time.time()
    # sequential()
    func = lambda name: read_file(name)
    multi_process(func)
    end = time.time()
    print('Total time: %0.2f seconds.' % (end - start))


