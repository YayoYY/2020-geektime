'''
队列：

基本操作：
1. 初始化
2. 求长
3. 入队
4. 出队

'''


class Queue():
    '''队列'''

    def __init__(self):
        self.__lst = []

    def is_empty(self):
        '''判空'''

        return self.__lst == []

    def size(self):
        '''求长'''

        return len(self.__lst)

    def travel(self):
        '''遍历'''

        return self.__lst

    def enqueue(self, item):
        '''进队'''

        self.__lst.insert(0, item)

    def dequeue(self):
        '''出队'''

        return self.__lst.pop()

if __name__ == '__main__':

    '''Queue'''

    q = Queue()

    q.enqueue(1)
    print("Enqueue 1:", q.travel())

    q.enqueue(2)
    print("Enqueue 2:", q.travel())

    q.enqueue(3)
    print("Enqueue 3:", q.travel())

    ans = q.dequeue()
    print("Dequeue:", q.travel(), ans)

