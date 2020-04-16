'''
二分查找
'''

def binary_search(lst, item):
    n = len(lst)
    L, R = 0, n - 1

    while L <= R:
        mid = (L + R) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            R = mid - 1
        else:
            L = mid + 1

    return -1

if __name__ == "__main__":
    lst = [1, 2, 3, 6, 7, 8]
    ans = binary_search(lst, 5)
    print("Binary search 5 in [1, 2, 3, 6, 7, 8],", ans)
    ans = binary_search(lst, 2)
    print("Binary search 2 in [1, 2, 3, 6, 7, 8],", ans)