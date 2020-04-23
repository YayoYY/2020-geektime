'''
LRU缓存淘汰机制：

LRU缓存淘汰机制（Least Recently Used）为最近最少使用缓存机制，即在缓存容量一定的情况下，
当有新的缓存数据时，删除最近的最少使用的数据。

LRU缓存淘汰机制可以使用哈希表+双向链表的实现机制，可以在插入数据和删除数据都达到O(1)的时间复杂度。

'''

class Node():
    '''双向链表结点'''

    def __init__(self, key=None, value=None):
        '''初始化
        Args:
            key: 键
            value: 值
        Self:
            key: 键
            value: 值
            prev: 前驱
            next: 后继
        '''
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    '''LRU缓存，最后使用的在尾部'''

    def __init__(self, capacity: int):
        '''初始化
        Args:
            capacity: 容量
        Self:
            capacity: 容量
            cache: 缓存数据，key为键，value为对应的链表结点
            head: 头结点
            tail: 尾结点
        '''

        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def delete_node(self, node):
        '''删除某一结点
        Args:
            node: 某一结点
        '''

        node.prev.next = node.next
        node.next.prev = node.prev

    def append_node(self, node):
        '''尾部插入某一结点
        Args:
            node: 某一结点
        '''

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int):
        '''获取某一个数据
        Args:
            key: 键
        Return:
            value: 值
        '''

        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
            self.append_node(node)
            return node.value

        else:
            return -1

    def put(self, key: int, value: int):
        '''插入某一数据
        Args:
            key: 键
            value: 值
        '''

        if key in self.cache: # 当数据存在
            node = self.cache[key]
            node.value = value # 改变数据的值
            self.delete_node(node) # 移动到最后
            self.append_node(node)

        elif len(self.cache) == self.capacity: # 不存在，但容量满了

            first = self.head.next
            self.cache.pop(first.key)
            self.delete_node(first) # 删除第一个结点
            node = Node(key, value)
            self.append_node(node)
            self.cache[key] = node # 插入新的数据

        else: # 容量没满
            node = Node(key, value)
            self.append_node(node)
            self.cache[key] = node