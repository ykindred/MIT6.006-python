def merge(A, B):
    L = []
    key_a = key_b = 0
    while True:
        if key_a >= len(A):
            L.extend(B[key_b:])
            return L
        elif key_b >= len(B):
            L.extend(A[key_a:])
            return L

        if A[key_a] > B[key_b]:
            L.append(B[key_b])
            key_b += 1
        else:
            L.append(A[key_a])
            key_a += 1



def merge_sort(A):
    """
    对数组A进行归并排序.
    一个时间复杂度O(nlog n)的稳定非原地排序.

    """
    # base case
    if len(A) <= 1:
        return A

    # recursion
    mid = len(A) // 2
    L = A[0:mid]
    R = A[mid:len(A)]
    L = merge_sort(L)
    R = merge_sort(R)
    return merge(L, R)
