'''
双链表：

基本操作：
1. 初始化：同单链表
2. 判空：同单链表
3. 求长：同单链表
4. 遍历：同单链表
5. 查找：同单链表
6. 头插
7. 尾插
8. 某一位置插入
9. 删除

'''

class Node():

    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class DoubleLinkList():
    '''双向链表'''

    def __init__(self, node=None):
        '''初始化'''

        self.__head = node

    def is_empty(self):
        '''判空'''

        return self.__head == None

    def length(self):
        '''求长'''

        cur, count = self.__head, 0

        while cur:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        '''遍历'''

        cur = self.__head
        lst = []

        while cur:
            lst.append(cur.val)
            cur = cur.next

        return lst


    def search(self, item):
        '''搜索'''

        cur, i = self.__head, -1

        while cur:
            i += 1

            if cur.val == item:
                return i

            cur = cur.next

        return i

    def add(self, item):
        '''头插'''

        node = Node(item)

        if self.is_empty():
            self.__head = node

        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, item):
        '''尾插'''

        node = Node(item)

        if self.is_empty():
            self.__head = node

        else:
            cur = self.__head

            while cur.next:
                cur = cur.next

            cur.next = node
            node.pre = cur

    def insert(self, pos, item):
        '''指定位置插'''

        if pos <= 0:
            self.add(item)

        elif pos >= self.length():
            self.append(item)

        else:
            node = Node(item)
            cur, i = self.__head, 0

            while i < pos:
                i += 1
                cur = cur.next

            pre = cur.pre
            node.pre = pre
            pre.next = node
            node.next = cur
            cur.pre = node

    def remove(self, item):
        '''移除元素'''

        cur = self.__head

        while cur:

            if cur.val == item:
                pre = cur.pre
                if pre == None:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.pre = None
                else:
                    pre.next = cur.next
                    if cur.next:
                        cur.next.pre = pre
                break

            cur = cur.next

if __name__ == '__main__':


    '''DoubleLinkList'''

    dll = DoubleLinkList()
    print("Travel:", dll.travel())
    print("Length:", dll.length())

    dll.append(1)
    print("Append 1:", dll.travel())
    print("Length:", dll.length())

    dll.append(2)
    print("Append 2:", dll.travel())

    dll.add(3)
    print("Add 3:", dll.travel())

    dll.insert(0, 4)
    print("Insert (0, 4):", dll.travel())

    dll.insert(2, 5)
    print("Insert (2, 5):", dll.travel())

    dll.insert(100, 6)
    print("Insert (100, 6):", dll.travel())
    print("Length:", dll.length())

    ans = dll.search(5)
    print("Search 5:", ans)

    dll.remove(3)
    print("Remove 3:", dll.travel())

    dll.remove(6)
    print("Remove 6:", dll.travel())

    dll.remove(3)
    print("Remove 3:", dll.travel())

    dll.remove(7)
    print("Remove 7:", dll.travel())

    dll.remove(4)
    print("Remove 4:", dll.travel())

    dll.remove(5)
    print("Remove 5:", dll.travel())

    dll.remove(2)
    print("Remove 2:", dll.travel())

    dll.remove(1)
    print("Remove 1:", dll.travel())
