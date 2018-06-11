"""
Self balancing binary search tree.

Summary:

    The following invariants are maintained throughout operations:

    1. Each node is colored red or black.
    2. Leaf nodes are colored black.
    3. If a node is red, then its children are black.
    4. Any path from a node to any of its leaves contains the same number of black colored nodes. I.e. the black height
       of any path from a node is the same.

    See operations section of wikipedia for details: wikipedia.org/wiki/Red–black_tree#Operations

Characteristics:

    * n number elements

    Search:
        Worst Time: O(logn)
    Insert:
        Worst Time: O(logn)
    Delete:
        Worst Time: O(logn)
"""

KEY_LEAF = object()


class Node(object):

    def __init__(self, key, val=None, color='r', parent=None, left=True, right=True):

        self.key = key
        self.val = val
        self.color = color

        self.parent = parent

        if left:
            self.left = Node(KEY_LEAF, color='b', parent=self, left=False, right=False)
        else:
            self.left = None

        if right:
            self.right = Node(KEY_LEAF, color='b', parent=self, left=False, right=False)
        else:
            self.left = None

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return self.create_string('  ')

    def __contains__(self, key):

        if self.is_leaf:
            return False

        if self.key == key:
            return True

        if key < self.key:
            return key in self.left
        return key in self.right

    def create_string(self, indent):
        string = str(self.key) + ' ' + self.color + '---+'
        if self.left.key is not KEY_LEAF:
            string += '\n(l)' + indent + self.left.create_string(indent + '    ')
        if self.right.key is not KEY_LEAF:
            string += '\n(r)' + indent + self.right.create_string(indent + '    ')
        return string

    def ordered_elems(self):

        parts = []

        if self.left.key is not KEY_LEAF:
            parts += self.left.ordered_elems()
        parts.append((self.key, self.val))
        if self.right.key is not KEY_LEAF:
            parts += self.right.ordered_elems()

        return parts

    @property
    def grandparent(self):
        return self.parent.parent

    @property
    def sibling(self):
        return self.parent.right if self is self.parent.left else self.parent.left

    @property
    def uncle(self):

        if self.parent.is_left_child:
            return self.grandparent.right

        return self.grandparent.left

    @property
    def is_left_child(self):

        return self.parent and self.parent.left is self

    @property
    def is_right_child(self):

        return self.parent and self.parent.right is self

    @property
    def is_leaf(self):
        return self.key is KEY_LEAF


def insert(root, key, val):

    node = Node(key, val)
    insert_add_node(root, node)

    insert_repair(node, root)

    while root.parent:
        root = root.parent

    return root


def insert_repair(node, root):

    if not node.parent:
        node.color = 'b'
    elif node.parent.color == 'b':
        pass
    elif node.uncle.color == 'r':
        # both parent and uncle are red
        node.parent.color = node.uncle.color = 'b'
        node.grandparent.color = 'r'
        insert_repair(node.grandparent, root)
    else:
        # parent red, uncle black
        if not node.grandparent.left.is_leaf and node is node.grandparent.left.right:
            # node is predecessor of grandparent in three gen subtree
            rotate_left(node.parent)
            node = node.left
        elif not node.grandparent.right.is_leaf and node is node.grandparent.right.left:
            # node is successor of grandparent in three gen subtree
            rotate_right(node.parent)
            node = node.right

        parent = node.parent
        grandparent = node.grandparent

        # now node is on outside of tree
        if node is parent.left:
            rotate_right(grandparent)
        else:
            rotate_left(grandparent)

        parent.color = 'b'
        grandparent.color = 'r'


def rotate_left(node):

    new_node = node.right
    parent = node.parent

    # update parent-new_node
    if parent:
        if parent.right is node:
            parent.right = new_node
        else:
            parent.left = new_node
    new_node.parent = parent

    # update node-right child
    node.right = new_node.left
    if node.right:
        node.right.parent = node

    # update new_node-node (left child)
    new_node.left = node
    new_node.left.parent = new_node


def rotate_right(node):

    new_node = node.left
    parent = node.parent

    # update parent-new_node
    if parent:
        if parent.right is node:
            parent.right = new_node
        else:
            parent.left = new_node
    new_node.parent = parent

    # update node-left child
    node.left = new_node.right
    if node.left:
        node.left.parent = node

    # update new_node-node (right child)
    new_node.right = node
    new_node.right.parent = new_node


def insert_add_node(root, node):

    if not root.is_leaf:
        if node < root:
            if not root.left.is_leaf:
                insert_add_node(root.left, node)
                return
            else:
                root.left = node
        else:
            if not root.right.is_leaf:
                insert_add_node(root.right, node)
                return
            else:
                root.right = node

    node.parent = root
    node.color = 'r'


def check_parents(root):

    if root.left:
        assert root.left.parent == root
        check_parents(root.left)
    if root.right:
        assert root.right.parent == root
        check_parents(root.right)


def get_min_max_heights(root: Node, level=0):

    if root.is_leaf:
        return level, level

    hleft = get_min_max_heights(root.left, level+1)
    hright = get_min_max_heights(root.right, level+1)

    return min(hleft[0], hright[0]), max(hleft[1], hright[1])


def delete(root, key):

    node = delete_get_node(root, Node(key))

    if node is None:
        raise KeyError

    if root.left.is_leaf and root.right.is_leaf:
        return

    # the new node will only have at most one non-leaf child
    node = replace_with_pred_or_succ(node)

    child = node.right if node.left.is_leaf else node.left

    child.parent = node.parent
    if node.is_left_child:
        node.parent.left = child
    else:
        node.parent.right = child

    if node.color == 'r' or child.color == 'r':
        child.color = 'b'
    else:
        # node black and child black -> child must be leaf here since replacement only has maximum one child
        delete_case1(child)

    root = child
    while root.parent:
        root = root.parent

    return root


def delete_case1(node):
    """Correct black height of paths through node (since it is 1 less than others)."""

    # if deleted node was root, then removed one black node from each path so black heights equal

    if node.parent:
        delete_case2(node)


def delete_case2(node):

    sibling = node.sibling

    if sibling.color == 'r':

        node.parent.color = 'r'
        sibling.color = 'b'

        if node.is_left_child:
            rotate_left(node.parent)
        else:
            rotate_right(node.parent)

    delete_case3(node)


def delete_case3(node: Node):

    sibling = node.sibling

    b = all([
        node.parent.color == 'b',
        sibling.color == 'b',
        sibling.left.color == 'b',
        sibling.right.color == 'b'
    ])

    if b:
        # coloring sibling red means all paths through parents have black height - 1
        sibling.color = 'r'
        # rebalance parent
        delete_case1(node.parent)
    else:
        delete_case4(node)


def delete_case4(node: Node):

    sibling = node.sibling

    b = all([
        sibling.parent.color == 'r',
        sibling.color == 'b',
        sibling.left.color == 'b',
        sibling.right.color == 'b'
    ])

    if b:
        # parent red, sibling black -> switching colors corrects black height through node by increasing it 1
        sibling.color = 'r'
        sibling.parent.color = 'b'
    else:
        delete_case5(node)


def delete_case5(node: Node):

    sibling = node.sibling

    # force sibling to be black with red child - this doesn't change black height
    if sibling.color == 'b':

        b1 = all([
            node.is_left_child,
            sibling.right.color == 'b',
            sibling.left.color == 'r'
        ])

        b2 = all([
            node.is_right_child,
            sibling.left.color == 'b',
            sibling.right.color == 'r'
        ])

        if b1:
            sibling.color = 'r'
            sibling.left.color = 'b'

            rotate_right(sibling)
        elif b2:
            sibling.color = 'r'
            sibling.right.color = 'b'

            rotate_left(sibling)

    delete_case6(node)


def delete_case6(node: Node):

    sibling = node.sibling

    # sibling's outside child is red

    sibling.color = node.parent.color
    node.parent.color = 'b'

    if node.is_left_child:
        sibling.right.color = 'b'
        rotate_left(node.parent)
    else:
        sibling.left.color = 'b'
        rotate_right(node.parent)


def replace_with_pred_or_succ(node: Node):

    if node.left.is_leaf and node.right.is_leaf:
        return node

    if node.left.is_leaf:
        replacement = node.right

        while not replacement.left.is_leaf:
            replacement = replacement.left
    else:
        replacement = node.left

        while not replacement.right.is_leaf:
            replacement = replacement.right

    node.key = replacement.key
    node.val = replacement.val

    return replacement


def delete_get_node(root: Node, node: Node):

    if root.is_leaf:
        return None

    if node < root:
        return delete_get_node(root.left, node)
    elif node > root:
        return delete_get_node(root.right, node)

    return root


if __name__ == '__main__':

    root = Node(0, 'foo', 'b')

    import random
    l = list(range(1, 1000))
    random.shuffle(l)

    for x in l:
        root = insert(root, x, 'bar')

    s = list(next(zip(*root.ordered_elems())))
    assert s == sorted(l + [0])

    print(get_min_max_heights(root))

    random.shuffle(l)
    for x in l:
        root = delete(root, x)

    print(root)
