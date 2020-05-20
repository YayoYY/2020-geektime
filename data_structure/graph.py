'''
图

1. 存储方式：
（1）邻接矩阵：二维矩阵
（2）邻接表：每一个节点对应一个链表

2. 遍历
（1）BFS：队列
（2）DFS：递归 / 栈（非递归）

'''

class Graph_Matrix():

    def __init__(self, mat):
        self.__n = len(mat)
        for x in mat:
            if len(x) != self.__n:
                return

        self.__mat = [mat[i][:] for i in range(self.__n)]

    def bfs(self):
        '''宽度优先遍历'''

        queue = [0] # 存储已访问过，但是相邻节点没有被访问过的元素
        visited = [0] # 存储已访问过的元素

        while queue:
            s = queue.pop(0) # 访问当前队首元素的相邻元素
            for i in range(self.__n):
                if self.__mat[s][i] != 0 and i not in visited:
                    visited.append(i)  # 标记该元素已经被访问
                    queue.append(i) # 将该元素入队，它的相邻元素没有访问过

        return visited


    def dfs_1(self):
        '''深度优先遍历（递归）'''

        visited = [] # 存储已访问过的元素
        def dfs(s):
            for t in range(self.__n):
                if t not in visited and self.__mat[s][t] != 0:
                    visited.append(t)
                    dfs(t)

        dfs(0)
        return visited

    def dfs_2(self):
        '''深度优先遍历（非递归）'''

        visited = [0]
        stack = [0]

        while stack:
            s = stack[-1]
            t = None
            for i in range(self.__n):
                if i not in visited and self.__mat[s][i] != 0:
                    t = i
                    break # 找到了一个没有被遍历的就退出
            if t: # 如果有还没被遍历的
                visited.append(i) # 访问该节点
                stack.append(i) # 将该节点入栈
            else:
                stack.pop() # 否则该节点的所有相连节点都被访问完了，该处理上一个节点了

        return visited

if __name__ == '__main__':

    graph = Graph_Matrix([[1, 0, 1, 1, 0, 0, 0],
                          [1, 1, 1, 0, 0, 1, 0],
                          [0, 1, 1, 0, 1, 0, 0],
                          [0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 0, 1, 0, 1],
                          [0, 0, 0, 0, 0, 1, 1],
                          [0, 0, 0, 0, 0, 0, 1]])

    ans = graph.bfs()
    print("BFS:", ans) # 0 2 3 1 4 5 6

    ans = graph.dfs_1()
    print("DFS1:", ans) # 0 2 1 5 6 4 3

    ans = graph.dfs_2()
    print("DFS2:", ans)  # 0 2 1 5 6 4 3