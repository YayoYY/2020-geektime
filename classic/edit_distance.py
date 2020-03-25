'''
编辑距离：

1. Levenshtein：
    把s1变为s2，最少需要的编辑次数。编辑可以是增加、删除、替换。
    eg: "mitcmu", "mtacnu", (对s1删除i，增加a，替换m为n，编辑距离为3)

2. Longest Common Substring（最长公共子串）：
    子串指原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    最长公共子串指s1和s2的共有的最长子串长度。从编辑距离角度理解，对应编辑的可以是增加、删除。
    eg: "mitcmu", "mtacnu", 4 (对s1删除i，增加a，删除m，"mtcu"，最长公共子串长度为4)

测试用例：
s1 = "mitcmu"
s2 = "mtacnu"
'''

global min_Dis
min_Dis = float('inf')
def levenshtein_backward(s1, s2, dis, i, j):
    '''莱文斯坦编辑距离（回溯）'''

    global min_Dis

    # 1.当s1走到结尾，dis+=s2剩余长度
    if s1[i:] == '':
        dis += len(s2[j:])
        if dis < min_Dis: min_Dis = dis
        return

    # 2.当s2走到结尾，dis+=s1剩余长度
    elif s2[j:] == '':
        dis += len(s1[i:])
        if dis < min_Dis: min_Dis = dis
        return

    # 当前字符相等，后移一位
    if s1[i] == s2[j]:
        levenshtein_backward(s1, s2, dis, i+1, j+1)
    else:
        # 选择1：删除s1[i]/添加s1[i]到s2，dis+=1（调用结束后dis,i,j本身没有变化，自动回溯）
        levenshtein_backward(s1, s2, dis+1, i+1, j)
        # 选择2：删除s2[j]/添加s2[j]到s1，dis+=1（（同上）
        levenshtein_backward(s1, s2, dis+1, i, j+1)
        # 选择3：替换，dis+=1，都后移（同上）
        levenshtein_backward(s1, s2, dis+1, i+1, j+1)

def levenshtein_dp(s1, s2):
    '''莱文斯坦编辑距离（动态规划）
    状态
        f(i, j)表示以s1[i], s2[j]结尾的字符串的编辑距离。

    状态转移方程
        f(0, j) = j, f(i, 0) = i: ""与s的编辑距离是len(s)
        if s1[i] == s2[j]: 如果当前字符串相等
            f(i, j) = min(f(i-1, j-1), 不用进行任何操作
                          f(i, j-1) + 1, s1前i位变成s2前j-1位，然后再插入一个s[j]
                          f(i-1, j) + 1), s1前i-1位变成s2前j位，然后再删除一个s[i]
        else: 如果当前字符串不相等
            f(i, j) = min(f(i-1, j-1) + 1, s1[i]替换位s2[j]
                          f(i, j-1) + 1, s1前i位变成s2前j-1位，然后再插入一个s[j]
                          f(i-1, j) + 1), s1前i-1位变成s2前j位，然后再删除一个s[i]
    '''

    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2+1) for _ in range(l1+1)]

    for j in range(1, l2+1):
        dp[0][j] = dp[0][j-1] + 1
    for i in range(1, l1+1):
        dp[i][0] = dp[i-1][0] + 1

    for i in range(1, l1+1):

        for j in range(1, l2+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)

    return dp[-1][-1]


global max_Length
max_Length = 0
def lcs_backward(s1, s2, length, i, j):
    '''最长公共子串编辑距离（回溯）

    '''
    global max_Length

    if s1[i:] == '' or s2[j:] == '':
        if length > max_Length:
            max_Length = length
        return

    if s1[i] == s2[j]:
        lcs_backward(s1, s2, length+1, i+1, j+1)
    else:
        lcs_backward(s1, s2, length, i+1, j)
        lcs_backward(s1, s2, length, i, j+1)

def lcs_dp(s1, s2):
    '''最长公共子串（动态规划）
    状态
        f(i, j)表示以s1[i], s2[j]结尾的字符串的最长公共子串。

    状态转移方程
        f(0, j) = j, f(i, 0) = i: ""与s的最长公共子串是0
        if s1[i] == s2[j]: 如果当前字符串相等
            f(i, j) = max(f(i-1, j-1) + 1, 最长公共子串长度加1
                          f(i, j-1), s1前i位与s2前j-1位的最长公共子串，然后再插入一个s[j]
                          f(i-1, j)), s1前i-1位与s2前j位的最长公共子串，然后再删除一个s[i]
        else: 如果当前字符串不相等
            f(i, j) = max(f(i-1, j-1), s1前i-1位与s2前j-1位的最长公共子串
                          f(i, j-1), s1前i位变成s2前j-1位，然后再插入一个s[j]
                          f(i-1, j)), s1前i-1位变成s2前j位，然后再删除一个s[i]
    '''
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2+1) for _ in range(l1+1)]

    for i in range(1, l1+1):

        for j in range(1, l2+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

if __name__ == "__main__":

    s1, s2 = "mitcmu", "mtacnu"

    levenshtein_backward(s1, s2, 0, 0, 0)
    print("levenshtein_backward: ", min_Dis)

    ans = levenshtein_dp(s1, s2)
    print("levenshtein_dp: ", ans)
    ans = levenshtein_dp("dinitrophenylhydrazine", "acetylphenylhydrazine")
    print("levenshtein_dp: ", ans, "(6)")
    ans = levenshtein_dp("sea", "eat")
    print("levenshtein_dp: ", ans, "(2)")

    lcs_backward(s1, s2, 0, 0, 0)
    print("lcs_backward", max_Length)

    ans = lcs_dp(s1, s2)
    print("lcs_dp: ", ans)