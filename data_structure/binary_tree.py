class TreeNode():

    def __init__(self, val):
        '''树节点'''

        self.val = val
        self.left = None
        self.right = None

class Binary_Tree():

    def __init__(self, node=None):
        '''二叉树'''

        self.__head = node

    def construct(self, mode, order1, order2=None):
        '''根据前/后序遍历、中序遍历，创建二叉树'''

        if mode == 'pi':
            self.__head = self.construct_1(order1, order2)
        elif mode == 'ip':
            self.__head = self.construct_2(order1, order2)
        else:
            self.construct_3(order1)


    def construct_1(self, preorder, inorder):
        '''根据前序遍历、中序遍历生成二叉树'''

        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        root.left = self.construct_1(preorder[1:1+i], inorder[:i])
        root.right = self.construct_1(preorder[1+i:], inorder[i+1:])
        return root

    def construct_2(self, postorder, inorder):
        '''根据后序遍历、中序遍历生成二叉树'''

        if not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.construct_2(postorder[:i], inorder[:i])
        root.right = self.construct_2(postorder[i:-1], inorder[i+1:])
        return root

    def construct_3(self, order):
        '''按层次构建二叉树'''

        if not order:
            return None

        self.__head = TreeNode(order[0])
        queue = [self.__head]
        i, n = 1, len(order)
        while queue:
            node = queue.pop(0)
            if i < n and order[i] != 'null':
                node.left = TreeNode(order[i])
                queue.append(node.left)
                i += 1
            if i < n and order[i] != 'null':
                node.right = TreeNode(order[i])
                queue.append(node.right)
                i += 1


    def bfs(self):
        '''广度优先遍历'''
        if not self.__head:
            return []

        ans = []
        queue = [self.__head]
        while queue:

            node = queue.pop(0)
            if node:
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return ans

    def dfs(self, mode):
        '''深度优先遍历'''

        ans = []
        if mode == 'pre':
            self.preorder(self.__head, ans)
        elif mode == 'in':
            self.inorder(self.__head, ans)
        else:
            self.postorder(self.__head, ans)

        return ans

    def preorder(self, node, ans):
        '''深度优先遍历：前序'''

        if not node:
            return
        ans.append(node.val)
        self.preorder(node.left, ans)
        self.preorder(node.right, ans)


    def inorder(self, node, ans):
        '''深度优先遍历：中序'''

        if not node:
            return
        self.inorder(node.left, ans)
        ans.append(node.val)
        self.inorder(node.right, ans)

    def postorder(self, node, ans):
        '''深度优先遍历：后序'''

        if not node:
            return
        self.postorder(node.left, ans)
        self.postorder(node.right, ans)
        ans.append(node.val)

if __name__ == '__main__':

    bt = Binary_Tree()
    bt.construct('pi', [9, 2, 7, 3, 6, 4, 8], [7, 2, 3, 9, 4, 6, 8])

    ans = bt.bfs()
    print("BFS:", ans)

    ans = bt.dfs('pre')
    print("PRE ORDER:", ans)

    ans = bt.dfs('in')
    print("IN ORDER:", ans)

    ans = bt.dfs('post')
    print("POST ORDER:", ans)

    bt = Binary_Tree()
    bt.construct('ip', [7, 3, 2, 4, 8, 6, 9], [7, 2, 3, 9, 4, 6, 8])

    ans = bt.bfs()
    print("BFS:", ans)

    ans = bt.dfs('pre')
    print("PRE ORDER:", ans)

    ans = bt.dfs('in')
    print("IN ORDER:", ans)

    ans = bt.dfs('post')
    print("POST ORDER:", ans)

    bt = Binary_Tree()
    bt.construct('l', [9, 2, 6, 7, 3, 4, 8])

    ans = bt.dfs('pre')
    print("PRE ORDER", ans)