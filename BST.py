class TreeNode:
    """
    :key: 该节点的键(或值)
    :num: 该值的数量
    :left: 指向左子树的指针
    :right: 指向右子树的指针
    """
    def __init__(self, key):

        self.key, self.num = key, 1
        self.left = None
        self.right = None

    def __repr__(self):
        return str_of_tree(self)


def str_of_tree(root: TreeNode, h = 0) -> str:
    """
    接收一个二叉树的根节点，返回整个树的可视化结构。
    :param root: 树的根节点
    :return: 字符串, 作为树的整个可视化结构
    """
    if root is None:
        return ''
    s = ''
    s += f"  Key:{root.key}({root.num})\n"
    s += h * '      ' + ' Left:'
    s += str_of_tree(root.left, h + 1)
    s += '\n'
    s += h * '      ' + 'Right:'
    s += str_of_tree(root.right, h + 1)
    return s


def insert(root: TreeNode, val: int) -> TreeNode:
    """
    通过myroot = insert(myroot, val)的方式向树中插入元素, 始终返回根节点
    :param root: 根节点
    :param val: 需要插入的值
    :return: 根节点
    """
    if root is None:
        return TreeNode(val)

    current = root
    while True:
        if current.key == val:
            current.num += 1
            return root
        elif val < current.key:
            if current.left is None:
                current.left = TreeNode(val)
                return root
            else:
                current = current.left
        elif val > current.key:
            if current.right is None:
                current.right = TreeNode(val)
                return root
            else:
                current = current.right


def search(root: TreeNode, val: int) -> TreeNode | None:
    """
    在树中搜索元素, 若找到返回该节点, 未找到返回None
    :param root: 根节点
    :param val: 搜索的值
    :return: 节点或None
    """
    if root is None:
        return None
    if val == root.key:
        return root

    current = root
    while True:
        if current is None:
            return None
        elif val == current.key:
            return current
        elif val > current.key:
            current = current.right
        elif val < current.key:
            current = current.left


def find_max(root: TreeNode) -> TreeNode | None:
    """
    找到树中的最大值
    :param root: 根节点
    :return: 空树返回None, 否则返回最大值节点
    """
    if root is None:
        return None

    current = root
    while True:
        if current.right is None:
            return current
        else:
            current = current.right


def find_min(root: TreeNode) -> TreeNode | None:
    """
    找到树中的最小值
    :param root: 根节点
    :return: 空树返回None, 否则返回最小值节点
    """
    if root is None:
        return None

    current = root
    while True:
        if current.left is None:
            return current
        else:
            current = current.left


def delete(root: TreeNode, val: int) -> TreeNode | None:
    """
    删除BST树中所有的某值
    :param root: BST树的根
    :param val: 需要删除的值
    :return: 删除后的根节点
    """
    if root is None:
        return None

    if val > root.key:
        root.right = delete(root.right, val)
    elif val < root.key:
        root.left = delete(root.left, val)
    elif val == root.key:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            new_root = find_min(root.right)
            root.key, new_root.key = new_root.key, root.key
            root.num, new_root.num = new_root.num, root.num
            root.right = delete(root.right, val)
    return root


def reduce(root: TreeNode, val: int) -> TreeNode | None:
    """
    使BST树中某值的数量减少1
    :param root: BST树的根
    :param val: 某值
    :return: 减少后的根节点
    """
    if root is None:
        return None

    if val > root.key:
        root.right = reduce(root.right, val)
    elif val < root.key:
        root.left = reduce(root.left, val)
    elif val == root.key:
        if root.num >= 2:
            root.num -= 1
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                new_root = find_min(root.right)
                root.key, new_root.key = new_root.key, root.key
                root.num, new_root.num = new_root.num, root.num
                root.right = delete(root.right, val)
    return root


def build_BST(arr: list) -> TreeNode:
    """
    从数组建立BST, 理想情况下复杂度为O(nlog n), 最差复杂度为O(n^2)
    :param arr: 数组
    :return: BST树的根节点
    """
    bst = None
    for i in arr:
        bst = insert(bst, i)
    return bst


def BST_sort(arr: list) -> list:
    """
    利用BST排序, 理想情况下复杂度为O(nlog n), 最差复杂度为O(n^2)
    :param arr: 数组
    :return: 排序后的数组
    """
    ans = []

    # 递归辅助函数
    def helper(root: TreeNode) -> None:
        if root is None:
            return
        helper(root.left)
        t = root.num
        while t:
            ans.append(root.key)
            t -= 1
        helper(root.right)
    helper(build_BST(arr))
    return ans