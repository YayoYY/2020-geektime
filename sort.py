'''
排序算法：

1. 冒泡排序：
    两两交换，每次大迭代将最大的放到最后
    最好O(n), 最坏O(n2), 平均O(n2), 稳定

2. 选择排序：
    每次选择最小的放到最前
    最好O(n2), 最坏O(n2), 平均O(n2), 不稳定

3. 插入排序：
    将未排序数字依次插入到已排序数字中
    最好O(n), 最坏O(n2), 平均O(n2), 稳定
    对比：比冒泡好，如果是其他语言中，冒泡的交换要进行三次操作，插入可以记录value从而只进行一次

4. 希尔排序：
    每隔一定步长做选择排序，逐渐缩短步长
    最好O(n1.3), 最坏O(n2), 不稳定

5. 快速排序：
    选择一个数字作为基准，将其左边数字都小于它，右边数字都大于它
    最好O(nlogn), 最坏O(n2), 平均O(nlogn), 不稳定

6. 归并排序：
    子数组分别排序，在合并到新的数组中
    最好O(nlogn), 最坏O(nlogn), 平均O(nlogn), 稳定
    对比：思路上，快排是自上而下，归并是自下而上，时间复杂度快排最坏时不好，空间复杂度上快排更好，稳定性比快排好

7. 堆排序：
    建堆、交换、堆化、交换...
    最好O(nlogn), 最坏O(nlogn), 平均O(nlogn), 不稳定
    对比：内存上没有快排友好，而且交换次数比快排多

8. 桶排序：
    将数据分到有序的桶内, 每个桶单独排序后，再将全部数据按序取出
    最好O(n), 最坏O(n), 平均O(n), 稳定

9. 计数排序：
    细粒度的桶排序
    最好O(n), 最坏O(n), 平均O(n), 稳定

10. 基数排序：
    先按低位排序, 逐渐升到⾼高位
    最好O(n), 最坏O(n), 平均O(n), 稳定

'''

def bubble_sort(lst):
    '''冒泡排序'''

    n = len(lst)

    for i in range(n):
        for j in range(n-i-1):

            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def select_sort(lst):
    '''选择排序'''

    n = len(lst)

    for i in range(n):
        k = i

        for j in range(i+1, n):
            if lst[k] > lst[j]:
                k = j

        lst[k], lst[i] = lst[i], lst[k]

def insert_sort(lst):
    '''插入排序'''

    n = len(lst)

    for i in range(1, n):
        for j in range(i, 0, -1):

            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

            else:
                break


def shell_sort(lst):
    '''希尔排序'''

    n = len(lst)
    s = 4

    while s > 0:

        for i in range(s, n):

            for j in range(i, 0, -s):
                if lst[j] < lst[j-s]:
                    lst[j], lst[j-s] = lst[j-s], lst[j]
                else:
                    break
        s //= 2

def quick_sort(lst, start, end):
    '''快速排序'''

    if start >= end:
        return

    L, R = start, end
    value = lst[L]

    while L < R:

        while value < lst[R] and R > L:
            R -= 1

        lst[L] = lst[R]

        while value >= lst[L] and R > L:
            L += 1

        lst[R] = lst[L]

    lst[R] = value
    quick_sort(lst, start, R-1)
    quick_sort(lst, R+1, end)


def merge_sort(lst):
    '''归并排序'''
    n = len(lst)

    if n <= 1:
        return lst

    mid = n // 2
    left_lst, right_lst = lst[:mid], lst[mid:]

    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    merge_lst = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_lst) and right_idx < len(right_lst):
        if left_lst[left_idx] <= right_lst[right_idx]:
            merge_lst.append(left_lst[left_idx])
            left_idx += 1
        else:
            merge_lst.append(right_lst[right_idx])
            right_idx += 1

    merge_lst += left_lst[left_idx:]
    merge_lst += right_lst[right_idx:]

    return merge_lst

def heap_sort(lst):
    '''堆排序'''
    from data_structure.heap import heap_sort

    heap_sort(lst)

def count_sort(lst):
    '''计数排序'''

    min, max = min(lst), max(lst)
    n = max - min + 1
    count = [0] * n

    for item in lst:
        idx = item - min
        count[idx] += 1

    new_lst = []
    for idx in range(n):
        while count[idx] != 0:
            new_lst.append(min + idx)
            count[idx] -= 1
    return new_lst

if __name__ == "__main__":

    ans = count_sort([12, 11, 13, 5, 6, 7])
    print(ans)

    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)

    lst = [3, 2, 6, 8, 4, 2, 9]
    bubble_sort(lst)
    print("bubble sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    select_sort(lst)
    print("select sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    insert_sort(lst)
    print("insert sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    quick_sort(lst, 0, len(lst)-1)
    print("quick sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    ans = merge_sort(lst)
    print("merge sort:", ans)

    lst = [3, 2, 6, 8, 4, 2, 9]
    shell_sort(lst)
    print("shell sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    heap_sort(lst)
    print("heap sort:", lst)

    lst = [3, 2, 6, 8, 4, 2, 9]
    ans = count_sort(lst)
    print("count sort:", ans)