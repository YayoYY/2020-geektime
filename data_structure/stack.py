'''
栈：

基本操作：
1. 初始化
2. 求长
3. 栈顶
4. 进栈
5. 出栈

'''

class Stack():
    '''栈'''

    def __init__(self):
        '''初始化'''

        self.__lst = []

    def size(self):
        '''求长'''

        return len(self.__lst)

    def travel(self):
        '''遍历'''

        return self.__lst

    def peek(self):
        '''栈顶'''

        if self.__lst:
            return self.__lst[-1]

    def push(self, item):
        '''进栈'''

        self.__lst.append(item)

    def pop(self):
        '''出栈'''

        if self.__lst:
            return self.__lst.pop()

if __name__ == '__main__':

    '''Stack'''

    s = Stack()

    s.push(1)
    print("Push 1:", s.travel())

    s.push(2)
    print("Push 2:", s.travel())

    s.push(3)
    print("Push 3:", s.travel())

    ans = s.pop()
    print("Pop:", s.travel(), ans)

    print("Peek:", s.peek())


