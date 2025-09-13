def max_heapify(A, x):
    """
    将堆A (A[0]储存堆元素个数n, 实际索引从1开始) 的某个违反堆序的节点x大根堆化.
    """
    lt = 2 * x
    rt = 2 * x + 1
    # 确定x, lt, rt中最大的, 并与x交换
    if lt <= A[0] and A[x] < A[lt]:
        largest = lt
    else:
        largest = x

    if rt <= A[0] and A[rt] > A[largest]:
        largest = rt

    # 如果并未交换, 说明x在正确位置上
    if x == largest:
        return

    # 否则则说明x在largest位置上, 递归
    A[x], A[largest] = A[largest], A[x]
    max_heapify(A, largest)

def build_max_heap(A):
    """
    从数组A建堆(索引从0开始)
    """
    # 保证堆的索引从1开始, A[0]储存堆的元素个数n.
    A.insert(0, len(A))

    # 从n / 2开始倒序遍历.
    i = A[0] // 2
    while i > 0:
        max_heapify(A, i)
        i -= 1

def insert(A, val):
    """
    向堆A(A[0]储存元素个数n, 索引从1开始)中插入值val
    """
    # 若数组大小不足, append, 反之则赋值
    idx = A[0] + 1
    if idx == len(A):
        A.append(val)
    else:
        A[idx] = val
    A[0] += 1

    # 上滤, 每次比较节点与其父节点
    while idx != 1 and A[idx] > A[idx // 2]:
        A[idx], A[idx // 2] = A[idx // 2], A[idx]
        idx = idx // 2

def top(A):
    """
    查询堆顶
    """
    return A[1]

def pop(A):
    """
    移除(塞至堆尾并size-1)并返回堆顶
    """
    last = A[0]
    A[1], A[last] = A[last], A[1]
    A[0] -= 1
    max_heapify(A, 1)
    return A[last]

def heap_sort(A):
    """
    对某数组A进行升序堆排序, 索引从0开始
    一种O(nlog n)的原地非稳定排序.
    """
    build_max_heap(A)
    while A[0] > 0:
        pop(A)      # 每次将最大元素塞至队尾
    del A[0]        # 将A恢复为数组