class TreeNode:
    """
    :key: 该节点的键(或值)
    :num: 该值的数量
    :left: 指向左子树的指针
    :right: 指向右子树的指针
    :height: 某节点的高度
    """
    def __init__(self, key):
        self.key = key
        self.num = 1
        self.left = None
        self.right = None
        self.height = 1

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


def get_height(node: TreeNode) -> int:
    """
    给出某一节点的高度
    :param node: 某节点
    """
    if node is None:
        return 0
    return node.height


def get_BF(node: TreeNode) -> int:
    """
    给出某节点的平衡因子
    :param node: 某节点
    :return: 平衡因子, 整数
    """
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotate(node: TreeNode) -> TreeNode:
    """
    对某子树做右旋, 返回右旋后的根节点
    :param node: 某节点
    :return: 右旋后的根节点
    """
    # 右旋时左子树不应为空
    assert not (node.left is None), "left child shouldn't be None"

    # 旋转
    new_root, new_right, new_right_left = node.left, node, node.left.right
    node, node.right, node.right.left = new_root, new_right, new_right_left

    # 更新高度
    new_root.right.height = 1 + max(get_height(new_root.right.left), get_height(new_root.right.right))
    new_root.height = 1 + max(get_height(new_root.left), get_height(new_root.right))

    return new_root


def left_rotate(node: TreeNode) -> TreeNode:
    """
    对某子树做左旋, 返回左旋后的根节点
    :param node: 某节点
    :return: 左旋后的根节点
    """
    # 左旋时右子树不应为空
    assert not (node.right is None), "right child shouldn't be None"

    # 旋转
    new_root, new_left, new_left_right = node.right, node, node.right.left
    node, node.left, node.left.right = new_root, new_left, new_left_right

    # 更新高度
    new_root.left.height = 1 + max(get_height(new_root.left.right), get_height(new_root.left.left))
    new_root.height = 1 + max(get_height(new_root.right), get_height(new_root.left))
    return new_root


def rotate(root: TreeNode) -> TreeNode:
    """
    对某节点做平衡检查, 若失衡则旋转
    :param root: 某节点
    :return: 检查后的根节点
    """
    BF = get_BF(root)
    left_BF = get_BF(root.left)
    right_BF = get_BF(root.right)

    if BF >= 2:
        # LL
        if left_BF == 1:
            root = right_rotate(root)
        # LR
        elif left_BF == -1:
            root.left = left_rotate(root.left)
            root = right_rotate(root)

    elif BF <= -2:
        # RR
        if right_BF == -1:
            root = left_rotate(root)
        # RL
        elif right_BF == 1:
            root.right = right_rotate(root.right)
            root = left_rotate(root)
    return root


def insert(root: TreeNode, val: int) -> TreeNode:
    """
    向AVL树中插入某值
    :param root: AVL树的根
    :param val: 某值
    :return: 插入后的根节点
    """
    # 标准BST插入
    if root is None:
        return TreeNode(val)

    if val == root.key:
        root.num += 1
    elif val > root.key:
        root.right = insert(root.right, val)
    elif val < root.key:
        root.left = insert(root.left, val)

    # 更新高度
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # 检查旋转
    root = rotate(root)

    return root


def delete(root: TreeNode, val: int) -> TreeNode | None:
    """
    删除AVL树中所有的某值
    :param root: AVL树的根
    :param val: 需要删除的值
    :return: 删除后的根节点
    """
    # 标准BST删除
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

    if not(root is None):
        # 更新高度
        root.height = 1 + max(get_height(root.left), get_height(root.right))

        # 检查旋转
        root = rotate(root)

    return root


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


def reduce(root: TreeNode, val: int) -> TreeNode | None:
    """
    使AVL树中某值的数量减少1
    :param root: AVL树的根
    :param val: 某值
    :return: 减少后的根节点
    """
    # 标准BST减少
    if root is None:
        return None

    if val > root.key:
        root.right = reduce(root.right, val)
    elif val < root.key:
        root.left = reduce(root.left, val)
    elif val == root.key:
        if root.num >= 2:
            root.num -= 1
            return root
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

    if not (root is None):
        # 更新高度
        root.height = 1 + max(get_height(root.left), get_height(root.right))

        # 检查旋转
        root = rotate(root)

    return root


def build_AVL(arr: list) -> TreeNode:
    """
    从数组建立AVL, 复杂度为O(nlog n)
    :param arr: 数组
    :return: AVL树的根节点
    """
    avl = None
    for i in arr:
        avl = insert(avl, i)
    return avl


def AVL_sort(arr: list) -> list:
    """
    利用AVL排序, 复杂度为O(nlog n)
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

    helper(build_AVL(arr))
    return ans