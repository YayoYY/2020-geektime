'''
循环队列

循环队列的一个好处是我们可以利用这个队列之前用过的空间。
在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。
但是使用循环队列，我们能使用这些空间去存储新的值。

循环队列的存储容器的容量要为最大容量+1。
head指向队首元素，rear指向即将插入的下一个位置。
如果head == rear，则说明队列为空。
如果rear的下一个位置就是head，则说明队列满了。

'''

class CircularQueue:

    def __init__(self, k: int):
        '''初始化'''

        self.__lst = [None] * (k + 1)
        self.k = k + 1
        self.head = 0
        self.rear = 0

    def enQueue(self, value: int):
        '''入队'''

        if not self.isFull():
            self.__lst[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            return True

        else:
            return False

    def deQueue(self):
        '''出队'''

        if not self.isEmpty():
            self.__lst[self.head] = None
            self.head = (self.head + 1) % self.k
            return True

        else:
            return False

    def Front(self):
        '''获取队首元素'''

        if not self.isEmpty():
            return self.__lst[self.head]

        else:
            return -1

    def Rear(self):
        '''获取队尾元素'''

        if not self.isEmpty():
            return self.__lst[(self.rear - 1 + self.k) % self.k]

        else:
            return -1

    def isEmpty(self):
        '''判空'''

        if self.head == self.rear:
            return True

        else:
            return False

    def isFull(self):
        '''判满'''

        if (self.rear + 1) % self.k == self.head:
            return True
        else:
            return False

if __name__ == '__main__':

    cq = CircularQueue(3)

    cq.enQueue(1)
    cq.enQueue(2)
    cq.enQueue(3)
    print("Enqueue 1 2 3")

    ans = cq.enQueue(4)
    print("Enqueue 4:", ans)

    ans = cq.Rear()
    print("Rear:", ans)

    ans = cq.isFull()
    print("Is Full?", ans)

    ans = cq.deQueue()
    print("Dequeue:", ans)

    ans = cq.Front()
    print("Front:", ans)