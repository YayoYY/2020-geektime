'''
单向循环链表：

基本操作：
1. 初始化
2. 判空
3. 求长
4. 遍历
5. 查找
6. 头插
7. 尾插
8. 某一位置插入
9. 删除

ps. 基本操作要考虑为结点的next是self.__head

'''

class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

class RSingleLinkList():
    '''单向循环链表'''

    def __init__(self, node=None):
        '''初始化'''

        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        '''判空'''

        return self.__head == None

    def length(self):
        '''求长'''

        cur, count = self.__head, 0

        while cur:
            count += 1
            cur = cur.next

            if cur == self.__head:
                break

        return count

    def travel(self):
        '''遍历'''

        cur = self.__head
        lst = []

        while cur:
            lst.append(cur.val)
            cur = cur.next

            if cur == self.__head:
                break

        return lst


    def search(self, item):
        '''搜索'''

        cur, i = self.__head, -1

        while cur:
            i += 1

            if cur.val == item:
                return i

            cur = cur.next

            if cur == self.__head:
                break

        return -1

    def add(self, item):
        '''头插'''

        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = self.__head

        else:

            last_node = self.__head.next

            while last_node.next != self.__head:
                last_node = last_node.next

            last_node.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item):
        '''尾插'''

        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = self.__head

        else:
            last_node = self.__head.next

            while last_node.next != self.__head:
                last_node = last_node.next

            last_node.next = node
            node.next = self.__head

    def insert(self, pos, item):
        '''指定位置插'''

        if pos <= 0:
            self.add(item)

        elif pos >= self.length():
            self.append(item)

        else:
            node = Node(item)
            cur, i = self.__head, 0

            while i < pos - 1:
                cur = cur.next
                i += 1

            node.next = cur.next
            cur.next = node

    def remove(self, item):
        '''移除元素'''

        cur = self.__head

        if not self.is_empty():
            last_node = self.__head

            while last_node.next != self.__head:
                last_node = last_node.next

        while cur:

            if cur.val == item:

                if cur == self.__head and cur == last_node:
                    self.__head = None

                elif cur == self.__head:

                    last_node.next = cur.next
                    self.__head = cur.next

                else:

                    pre = self.__head

                    while pre.next != cur:
                        pre = pre.next

                    pre.next = cur.next

                break

            cur = cur.next

            if cur == self.__head:
                break

if __name__ == '__main__':


    '''DoubleLinkList'''

    rsll = RSingleLinkList()
    print("Travel:", rsll.travel())
    print("Length:", rsll.length())

    rsll.append(1)
    print("Append 1:", rsll.travel())
    print("Length:", rsll.length())

    rsll.append(2)
    print("Append 2:", rsll.travel())

    rsll.add(3)
    print("Add 3:", rsll.travel())

    rsll.insert(0, 4)
    print("Insert (0, 4):", rsll.travel())

    rsll.insert(2, 5)
    print("Insert (2, 5):", rsll.travel())

    rsll.insert(100, 6)
    print("Insert (100, 6):", rsll.travel())
    print("Length:", rsll.length())

    ans = rsll.search(5)
    print("Search 5:", ans)

    ans = rsll.search(100)
    print("Search 100:", ans)

    rsll.remove(3)
    print("Remove 3:", rsll.travel())

    rsll.remove(6)
    print("Remove 6:", rsll.travel())

    rsll.remove(3)
    print("Remove 3:", rsll.travel())

    rsll.remove(7)
    print("Remove 7:", rsll.travel())

    rsll.remove(4)
    print("Remove 4:", rsll.travel())

    rsll.remove(5)
    print("Remove 5:", rsll.travel())

    rsll.remove(2)
    print("Remove 2:", rsll.travel())

    rsll.remove(1)
    print("Remove 1:", rsll.travel())
