def insertion_sort_swap(A):
    """
    对数组A进行插入排序, 使用交换实现.
    一种O(n^2)的原地排序.
    """
    for key in range(len(A)):
        val = A[key]
        # 将A[key]处的数插入至A[0:key - 1]中正确的位置
        i = key - 1
        while i > -1 and A[i] > val:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = val
    return A


def insertion_sort_binary(A):
    """
    对数组A进行插入排序, 使用二分实现.
    一种O(n^2)的原地排序.
    """
    # 共n次
    for key in range(len(A)):
        val = A[key]
        del A[key]
        # 将A[key]处的数插入至A[0:key - 1]中正确的位置
        l, r = -1, key
        mid = (l + r) // 2
        # 二分查找, 单次O(log n)
        while not r == l + 1:
            if A[mid] <= val:
                l = mid
            else:
                r = mid
            mid = (l + r) // 2
        # 插入, 单次O(n)
        A.insert(mid + 1, val)
    return A