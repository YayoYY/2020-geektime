'''
0/1背包问题：

n个物品，重量为weights=[w1, w2, ..., wn]，价值为values=[v1, v2, ..., vn]
现有给定容量为capacity的背包，如何让背包里装入的物品价值总和最大？


测试用例：
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
'''

def knapsack_dp(weights, values, capacity):
    '''动态规划求解
    状态
        f(i, j): 背包剩余容量为j时、前i个物品的最大价值总和
    状态转移方程
        f(0, j) = 0: 背包剩余容量为j时、前0个物品的最大价值总和为0
        f(i, 0) = 0: 背包剩余容量为0时、前i个物品的最大价值总和为0
        if weights[i] > j: 当前决策的物品重量大于背包剩余容量j时
            f(i, j) = f(i - 1, j): 不能装，价值与上一物品同等剩余容量相同时
        else:
            f(i, j) = max(f(i - 1, j), f(i - 1, j - weights[i]) + values[i]):
            重量为不装当前物品的总重量、装当前物品的总重量之中最大的一个。
            !!!注意!!!，如果装，想要得到当前剩余重量为j，需要在j-weight的基础上加当前物品的价值。
    ps. 可以先尝试通过回溯搜索看一个问题是否能够用动态规划求解。先画出搜索树：
        节点是状态与解f(x1, x2, ..., y)，边是决策{s1, s2, ...}，每一层是当前决策可能遇到的所有状态。
        如果搜索树中出现重复的状态，则可用动态规划求解（但有时自己使用的例子不会出现重复状态）。
        当一个问题确定可通过动态规划求解，之后的重点在于定义状态和状态转移矩阵（此状态与搜索树中的不同）。
    '''
    n = len(weights)
    dp = [[0 for j in range(capacity+1)] for i in range(n+1)]
    for i in range(1, n+1):
        weight = weights[i-1]
        for j in range(1, capacity+1):
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + values[i-1])
    return dp[-1][-1]

if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    ans = knapsack_dp(weights, values, capacity)
    print(ans)