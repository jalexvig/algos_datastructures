"""
For quickish lookups.

Summary:

    Store key/values. All nodes (keys) in left subtree must be less than node's key. All nodes (keys) in right subtree
    must be greater than node's key.

    Add is straightforward.
    Deletion involves finding successor node (node with next highest key) and swapping that node for the node to be
    deleted.

    **Note**: Worst case performance is bad since the tree can grow linearly.

Characteristics:

    * n number elements

    Search:
        Average Time: O(logn)
        Worst Time: O(n)
    Add:
        Average Time: O(logn)
        Worst Time: O(n)
    Delete:
        Average Time: O(logn)
        Worst Time: O(n)
"""


class Node(object):

    def __init__(self, key, val, left=None, right=None):

        self.key = key
        self.val = val

        self.left = left
        self.right = right

    def __getitem__(self, key):

        if self.key == key:
            return self.val

        if key < self.key and self.left:
            return self.left[key]

        if key > self.key and self.right:
            return self.right[key]

        raise KeyError

    # https://stackoverflow.com/questions/37426935
    def __str__(self):
        return self.create_string('  ')

    def create_string(self, indent):
        string = str(self.key) + '---+'
        if self.left:
            string += '\n(l)' + indent + self.left.create_string(indent + '    ')
        if self.right:
            string += '\n(r)' + indent + self.right.create_string(indent + '    ')
        return string

    def __contains__(self, item):

        if self.key == item:
            return True

        res = (item in self.left if self.left else False) or (item in self.right if self.right else False)

        return res


def add(key, val, node=None):

    if node is None:
        return Node(key, val)

    if node.key == key:
        return Node(key, val, node.left, node.right)

    if key < node.key:
        return Node(node.key, node.val, add(key, val, node.left), node.right)

    return Node(node.key, node.val, node.left, add(key, val, node.right))


def delete(key, root):

    if root is None:
        return root

    if key < root.key:
        root.left = delete(key, root.left)
    elif key > root.key:
        root.right = delete(key, root.right)
    else:

        if root.right is None:
            return root.left
        elif root.left is None:
            return root.right

        min_node = root.right
        while min_node.left:
            min_node = min_node.left

        root.key = min_node.key
        root.val = min_node.val

        root.right = delete(root.key, root.right)

    return root


def delete_loop(key, root):

    # This is messier but does only single traversal to find successor.

    node = root

    prev, dxn = None, None

    while node and node.key != key:
        prev = node
        node, dxn = (node.left, 'left') if node.key > key else (node.right, 'right')

    if node is None:
        raise KeyError

    succ_parent, succ = _get_succ(node)

    if succ:
        node.key = succ.key
        node.val = succ.val

        if succ_parent:
            succ_parent.left = None
        else:
            # node is succ_parent
            node.right = succ.right

        return root
    elif prev:
        setattr(prev, dxn, node.left)
        return root
    else:
        return node.left


def _get_succ(node):

    prev = None
    node = node.right

    while node and node.left:
        prev = node
        node = node.left

    return prev, node


if __name__ == '__main__':

    bst = add('d', 0)
    bst = add('b', 0, bst)
    bst = add('a', 0, bst)
    bst = add('c', 0, bst)
    bst = add('g', 0, bst)
    bst = add('e', 0, bst)
    bst = add('f', 0, bst)
    bst = add('h', 0, bst)

    print(bst)

    bst = delete('g', bst)

    print(bst)
