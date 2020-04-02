'''
字符串匹配：

1. BF算法(Brute Force)：暴力匹配
    对主串从i=0扫描，看以每一位开始的字符串是否能和模式串匹配。
    时间复杂度O(m*n)。

2. RK算法(Rabin-Karp)：暴力匹配+哈希函数
    对主串从i=0扫描，看以每一位开始的字符串与模式串的哈希值是否相等，如果相等在判断一下原串消解哈希冲突。
    时间复杂度O(m)。

3. BM算法(Boyer-Moore)：多滑动几位
    从后向前比较模式串字符和主串字符
    坏字符原则：当匹配到坏字符的时候，向后滑动到坏字符最后一次在模式串中出现的位置。
              （利用'bc'哈希表存储模式串中字符最后一次出现的位置）
    好后缀原则：当有好后缀的时候，向后滑动到好后缀最后一次在模式串中出现的位置。
              如果没有好后缀，则还需判断好后缀的后缀子串和模式串的前缀子串是否有匹配，有匹配则滑动到后缀子串位置。
              （利用'suffix'哈希表存储长度为i的后缀在模式串中最后一次出现的下标，
                利用'prefix'哈希表存储长度为i的后缀子串是否有对应的前缀子串）
    综合坏字符和好后缀的移动位数，最大的是模式串滑动的位置。

4. KMP算法(Knuth Morris Pratt)：多滑动几位
    从前向后比较模式串字符和主串字符
    pnext数组保存了长度为j的模式串，前j-1位和主串匹配而第j位与主串不匹配时，模式串应该回溯的位置k。
    pnext[j] = k，表示长度为j的字符串前缀子串与后缀子串（子串长度小于长长度）最长能匹配的位数。
    eg. "abbcabcaabbcaa"，pnext = [-1, 0, 0, 0, 0, 1, 2, 0, 1, 1, 2, 3, 4, 5]
    将j回溯到k能够保证前k-1位与模式串的后k-1位匹配，进而从第k位匹配即可。
    eg. "abcabd"，当d不匹配时，此时j是5，next[5] = 2，进而从j=2即c开始匹配即可。
    pnext数组的计算用动态规划的思想：
    if s[j] == s[k]：pnext[j] = k，
    if s[j] != s[k]：k = pnext[k]。直到k=-1时，k=0，pnext[j]=k（可匹配的长度为0）

测试用例；
main = "abcacabdc"
mode = "abd"

Args:
    main: 主串
    mode: 模式串
Return:
    pos: 匹配则返回初始下标；不匹配返回-1。
'''

def bf_string_match(main, mode):
    '''BF算法'''

    n, m, pos = len(main), len(mode), -1

    for i in range(n-m+1):

        match = True

        for j in range(m):

            if main[i+j] != mode[j]:
                match = False

        if match:
            pos = i
            break

    return pos

def rk_string_match(main, mode):
    '''RK算法'''

    # 字符串的哈希值 = 所有字符ascii值的和
    hash = lambda s: sum([ord(item) for item in s])

    n, m, ans = len(main), len(mode), -1
    hash_mode = hash(mode)

    for i in range(n-m+1):

        if hash(main[i:i+m]) == hash_mode:

            if main[i:i+m] == mode: # 若哈希值相等，再判断是否出现哈希冲突
                ans = i

    return ans

def bm_string_match(main, mode):
    '''BM算法'''

    n, m, pos = len(main), len(mode), -1

    # 坏字符的bc哈希表：存储模式串中每个字符最后出现的位置
    def generate_bc():
        '''坏字符准则辅助bc哈希表'''
        bc = {}

        for i in range(m-1, -1, -1):

            if mode[i] not in bc:
                bc[mode[i]] = i

        return bc

    # 好前缀的suffix哈希表：存储模式串中长度为i的每个后缀子串最后一次出现的下标
    # 好前缀的prefix数组：存储模式串中每个后缀子串是否与前缀子串匹配
    def generate_gs():
        '''好后缀辅助suffix、prefix哈希表'''

        suffix, prefix = {}, {}

        for i in range(m-1, -1, -1):

            l = m - i # 后缀子串长度

            for j in range(i-1, -1, -1): # 从前一个字符开始比较

                if mode[i:] == mode[j:j+l]:
                    suffix[l] = j

                    if j == 0:
                        prefix[l] = True

                    break

        return suffix, prefix

    bc = generate_bc()
    suffix, prefix = generate_gs()

    i = 0
    while i < n-m+1:

        match = True
        for j in range(m-1, -1, -1):

            if mode[j] != main[i+j]:

                bad_char = main[i+j] # 坏字符
                if bad_char in bc: # 如果mode中有坏字符
                    bad_move = j - bc[bad_char] # 滑动到最后一次出现的位置
                else: # 否则
                    bad_move = j + 1 # 滑动到头

                good_string = mode[j+1:] # 好后缀
                l = m - j - 1 # 好后缀长度
                good_move = 0
                if good_string: # 如果有好后缀
                    if l in suffix: # 如果mode中有好后缀
                        good_move = j + 1 - suffix[l] # 滑动到最后一次出现的位置
                    else: # 否则
                        for k in range(l-1, -1, -1): # 看好后缀的子串是否为mode的前缀
                            if k in prefix:
                                good_move = m - k # 有则移动到该位置
                    if good_move == 0: # 好后缀在前面没出现过，模式串整个滑动到现在的右边
                        good_move = m

                i += max(bad_move, good_move)
                match = False
                break

        if match:
            pos = i
            break

    return pos


def kmp_string_match(main, mode):
    '''KMP算法'''

    n, m, pos = len(main), len(mode), -1

    def generate_pnext():
        pnext = [-1] * m

        j, k = 0, -1
        while j < m - 1: # 只需计算前m-1个字符的pnext数组即可

            if k == -1 or mode[j] == mode[k]:
                j, k = j+1, k+1
                pnext[j] = k

            else:
                k = pnext[k]

        return pnext

    pnext = generate_pnext()

    i, j = 0, 0
    while i < n and j < m:

        if j == -1 or main[i] == mode[j]: # 当j==-1时，说明模式串开始从头开始匹配
            i, j = i+1, j+1

        else:
            j = pnext[j]

    if j == m: # 判断是否匹配到末尾
        pos = i - m

    return pos




ans = bf_string_match("abcacabdc", "abd")
print("BF:", ans)

ans = rk_string_match("abcacabdc", "abd")
print("RK:", ans)

ans = bm_string_match("abcacabdc", "cbca")
print("BM:", ans)

ans = kmp_string_match("abcacabdc", "bbca")
print("KMP:", ans)