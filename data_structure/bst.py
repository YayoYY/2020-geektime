'''
二叉搜索树

1. 构建：根据列表构建
2. 查找：根据与节点的大小搜索左右子树
3. 插入：根据与节点的比较，选择插入左还是右，插入到正好左、右为空的位置
4. 删除：如果没有孩子节点，删除即可；如果有一个孩子节点，用孩子节点替换；如果有多个孩子节点，用右子树最小的节点替换。

'''
from data_structure.binary_tree import *

class BST():

    def __init__(self, lst=[]):
        '''初始化（构建BST）'''

        lst = sorted(lst)
        self.__head = self.build_BST(lst)

    def build_BST(self, lst):
        '''构建BST'''

        if not lst:
            return None

        n = len(lst)
        mid = n // 2
        root = TreeNode(lst[mid])
        root.left = self.build_BST(lst[:mid])
        root.right = self.build_BST(lst[mid+1:])
        return root

    def insert(self, value):
        '''插入'''

        if not self.__head:
            self.__head = TreeNode(value)

        else:
            node = self.__head
            while True:
                if value < node.val:
                    if not node.left:
                        node.left = TreeNode(value)
                        break
                    else:
                        node = node.left
                        continue
                else:
                    if not node.right:
                        node.right = TreeNode(value)
                        break
                    else:
                        node = node.right
                        continue

    def bfs(self):
        '''广度优先遍历'''
        if not self.__head:
            return []

        ans = []
        queue = [self.__head]
        while queue:

            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                ans.append(node.val)
            else:
                ans.append("null")

        return ans

if __name__ == '__main__':
    bst = BST([2, 4, 6, 8, 4, 2, 1])
    ans = bst.bfs()
    print(ans)

    bst.insert(10)
    ans = bst.bfs()
    print(ans)

    bst.insert(5)
    ans = bst.bfs()
    print(ans)