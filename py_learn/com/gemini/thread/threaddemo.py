import threading as thread
import time


# 多线程
def fun1(a):
    for i in range(0, 50):
        time.sleep(1)
        print(thread.current_thread().getName(), i)


def fun2():
    for i in range(65, 76):
        print(thread.current_thread().getName(), chr(i))


# 找对象  找线程

print(thread.enumerate())


# 创建两个线程
# thread1 = thread.Thread(None,fun1,"线程1",args=(1,))
# thread2 = thread.Thread(None,fun2,"线程2")
# thread1.start();
# thread2.start();

class Mythread(thread):
    def __init__(self, a,name):
        super().__init__(name=name)  # 代表父类对象
        #thread.Thread.__init__(self,name=name)
        self.a = a

    def run(self):
            fun1(self.a)

thread3 = Mythread(1,"sd")
thread3.start()