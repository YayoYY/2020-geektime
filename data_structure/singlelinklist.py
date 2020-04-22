'''
单链表：

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

'''

class Node():
    '''结点'''

    def __init__(self, val):
        '''初始化'''

        self.val = val
        self.next = None

class SingleLinkList():
    '''单链表'''

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

        cur, lst = self.__head, []

        while cur:
            lst.append(cur.val)
            cur = cur.next

        return lst

    def search(self, item):
        '''查找'''

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
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''尾插'''

        if self.is_empty():
            self.__head = Node(item)

        else:
            cur = self.__head

            while cur.next:
                cur = cur.next

            cur.next = Node(item)

    def insert(self, pos, item):
        '''指定位置插入'''


        if pos <= 0:
            self.add(item)

        elif pos >= self.length():
            self.append(item)

        else:
            cur, i = self.__head, 0

            while cur and i < pos - 1:
                cur = cur.next
                i += 1

            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        '''删除'''

        pre, cur = None, self.__head

        while cur:
            if cur.val == item:
                if not pre:
                    self.__head = self.__head.next

                else:
                    pre.next = cur.next

                break

            else:
                pre, cur = cur, cur.next

if __name__ == '__main__':


    '''SingleLinkList'''

    sll = SingleLinkList()
    print("Travel:", sll.travel())
    print("Length:", sll.length())

    sll.append(1)
    print("Travel:", sll.travel())
    print("Length:", sll.length())

    sll.append(2)
    print("Append 2:", sll.travel())

    sll.add(3)
    print("Add 3:", sll.travel())

    sll.insert(0, 4)
    print("Insert (0, 4):", sll.travel())

    sll.insert(1, 5)
    print("Insert (1, 5):", sll.travel())

    sll.insert(100, 6)
    print("Insert (100, 6):", sll.travel())
    print("Length:", sll.length())

    ans = sll.search(5)
    print("Search 5:", ans)

    sll.remove(4)
    print("Remove 4:", sll.travel())

    sll.remove(6)
    print("Remove 6:", sll.travel())

    sll.remove(3)
    print("Remove 3:", sll.travel())

    sll.remove(7)
    print("Remove 7:", sll.travel())
