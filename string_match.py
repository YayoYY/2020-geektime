'''
字符串匹配：

1. BF算法(Brute Force)：暴力匹配。
    对主串从i=0扫描，看以每一位开始的字符串是否能和模式串匹配。

2. RK算法(Rabin-Karp)：暴力匹配+哈希函数

3. BM算法(Boyer-Moore)：

4. KMP算法(Knuth Morris Pratt)：

测试用例；
main = "abcacabdc"
mode = "abd"
'''

def bf_string_match(main, mode):
    '''BF算法
    Args:
        main: 主串
        mode: 模式串
    Return:
        pos: 匹配则返回初始下标；不匹配返回-1。
    '''
    n, m, pos = len(main), len(mode), -1
    for i in range(n-m+1):
        match = True
        for j in range(m):
            if main[i+j] != mode[j]:
                match = False
        if match:
            pos = i
    return pos

def rk_string_match(main, mode):
    '''RK算法
    Args:
        main: 主串
        mode: 模式串
    Return:
        pos: 匹配则返回初始下标；不匹配返回-1。
    '''
    # 字符串的哈希值=所有字符ascii值的和
    hash = lambda s: sum([ord(item) for item in s])

    n, m, ans = len(main), len(mode), -1
    hash_mode = hash(mode)
    for i in range(n-m+1):
        if hash(main[i:i+m]) == hash_mode:
            if main[i:i+m] == mode: # 若哈希值相等，再判断是否出现哈希冲突
                ans = i
    return ans

def bm_string_match(main, mode):
    n, m, ans = len(main), len(mode), -1
    # 坏字符的bc哈希表：存储模式串中每个字符最后出现的位置
    bc = {}
    for i in range(m-1, -1, -1):
        if mode[i] not in bc:
            bc[mode[i]] = i
    # 好前缀的suffix哈希表：存储模式串中长度为i的每个后缀子串最后一次出现的下标
    # 好前缀的prefix数组：存储模式串中每个后缀子串是否与前缀子串匹配
    suffix, prefix = {}, {}
    for i in range(1, m):
        suffix_mode = mode[m-i:]
        for j in range(i+1, m+1):
            if mode[m-j:m-j+i] == suffix_mode:
                suffix[i] = m-j
                break
        if mode[:i] == suffix_mode:
            prefix[i] = True
        else:
            prefix[i] = False
    prefix[m] = True

    i = m-1
    while i < n:
        i_move = 0
        for j in range(m-1, -1, -1): # 从后向前匹配
            if main[i-(m-1-j)] != mode[j]:
                # 计算坏字符规则下的移动位数
                if main[i] in bc:
                    i_1 = j - bc[main[i]]
                else:
                    i_1 = j + 1
                # 如果有好后缀的话，计算好后缀下的移动位数
                i_2 = 0
                if m-1-j > 0:
                    if m-1-j in suffix:
                        i_2 = j + 1 - suffix[m-1-j]
                    else:
                        for k in range(j+1, m+1):
                            if prefix[k]:
                                i_2 = k
                i_move = max(i_1, i_2)
                break
        if i_move == 0:
            ans = i-m+1
            break
        else:
            i += i_move

    return ans

def kmp_string_match(main, mode):
    pass


ans = bf_string_match("abcacabdc", "abd")
print("BF:", ans)

ans = rk_string_match("abcacabdc", "abd")
print("RK:", ans)

ans = bm_string_match("abcacabdc", "cacab")
print("BM:", ans)

ans = kmp_string_match("abcacabdc", "abd")
print("KMP:", ans)

