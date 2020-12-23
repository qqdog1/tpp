import threading
import time


class abc:
    def __init__(self):
        self.value = 0

    def value(self):
        return self.value;

    def add(self):
        self.value += 1


if __name__ == '__main__':
    aaa = abc()
    print(aaa.value)

    for n in range(100):
        t = threading.Thread(target=aaa.add)
        t.start()
        print('thread1 :', aaa.value)

