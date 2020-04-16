'''
堆：

1. 定义：父节点小于等于子节点的完全二叉树为小顶堆，大于等于子节点的完全二叉树为大顶堆。
2. 存储：堆用数组存储，若某一节点的下标为i，则左孩子为2i+1，右孩子为2i+2。
3. 基本操作：以小顶堆为练习
    （1）堆化（复杂度O(n)，推导见笔记）
        两种方法：
        第一种是自下而上的插入的思想，将每个元素插入到前面序列中（前面是已经建好的堆）
        第二种是自上而下的交换思想，从非叶子节点开始自上而下的交换
    （2）插入（复杂度O(logn)）
        先插入到最后，再自下而上的堆化
    （3）弹出堆顶元素（复杂度O(logn)）
        先保存第一个元素，再将最后一个元素移动到第一位，再上而下的堆化
    （4）堆排序（复杂度O(nlogn)）
        如果是升序排序，构建一个大顶堆，依次将元素的第一位（当前最大值）与最后的位置、倒数第二的位置...交换
        然后对前面的元素进行自上而下的堆化
        如果是降序排序，构建一个小顶堆，流程同上
        对比：堆排序没有快排好，其1, 2, 4的索引形式对内存不友好，且交换次数比快排多

'''

def bu_heapify(lst, i):
    '''自底向上的堆化，将i位置与其父节点比较交换，直至对应的位置
    Args:
        lst: 数组
        i: 当前需要堆化的位置
    '''
    if i == 0:
        return

    root_idx = i // 2 if i % 2 == 1 else i // 2 - 1
    if lst[root_idx] > lst[i]:
        lst[root_idx], lst[i] = lst[i], lst[root_idx]
        bu_heapify(lst, root_idx)

def td_heapify(lst, i, n=None):
    '''自顶向下的堆化，将i位置与其子节点比较交换，直至对应的位置
    Args:
        lst: 数组
        i: 当前需要堆化的位置
    '''
    if not n:
        n = len(lst)

    if i >= n:
        return

    idx, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and lst[l] < lst[idx]:
        idx = l
    if r < n and lst[r] < lst[idx]:
        idx = r
    if idx != i:
        lst[i], lst[idx] = lst[idx], lst[i]
        td_heapify(lst, idx)

def heapify(lst, mode='bu'):
    '''建堆
    Args:
        lst: 数组
    '''
    n = len(lst)

    if mode == 'bu':
        for i in range(n):
            bu_heapify(lst, i)

    else:
        begin_idx = (n - 1) // 2 if (n - 1) % 2 == 1 else (n - 1) // 2 - 1
        for i in range(begin_idx, -1, -1):
            td_heapify(lst, i)

def heappush(lst, item):
    '''插入
    Args:
        lst: 堆
        item: 插入的元素
    '''
    lst.append(item)
    i = len(lst) - 1
    bu_heapify(lst, i)

def heappop(lst):
    '''弹出堆顶元素
    Args:
        lst: 堆
    Return:
        item: 堆顶元素
    '''

    item = lst[0]
    lst[0] = lst.pop()
    td_heapify(lst, 0)
    return item

def heap_sort(lst):
    '''堆排序
    Args:
        lst: 堆
    '''
    heapify(lst)
    n = len(lst)
    for i in range(n-1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        td_heapify(lst, 0, i)

if __name__ == "__main__":

    a = [3, 4, 6, 2, 1]
    heapify(a)
    print("Bottom up heapify: [3, 4, 6, 2, 1]", a)

    a = [3, 4, 6, 2, 1]
    heapify(a, mode='td')
    print("Top down heapify: [3, 4, 6, 2, 1]", a)

    heappush(a, 1)
    print("Push \'1\':", a)

    ans = heappop(a)
    print("Pop:", a, ans)
    ans = heappop(a)
    print("Pop:", a, ans)
    ans = heappop(a)
    print("Pop:", a, ans)
    ans = heappop(a)
    print("Pop:", a, ans)

    a = [3, 4, 6, 2, 1]
    heap_sort(a)
    print("Heap sort: [3, 4, 6, 2, 1]", a)
