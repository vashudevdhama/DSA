'''
Insertion in Binary Search Tree - Recursive approach
'''
# class Node:
#     def __init__(self, value=None):
#         '''
#         :value: data value of node.
#         :left: left child of the node.
#         :right: right child of the node.
#         '''
#         self.value = value
#         self.left = None
#         self.right = None


def insert(root, node):
    '''
    :param root: root node of the bst.
    :param node: node to be inserted in bst.
    '''
    if not root:
        root = node
        return root
    else:
        return insertNode(root, node)


def insertNode(current, node):
    '''
    :param current: current node.
    :param node: node to be inserted.
    '''
    if node.value < current.value:
        if not current.left:
            current.left = node
        else:
            return insertNode(current.left, node)
    else:
        if not current.right:
            current.right = node
        else:
            return insertNode(current.right, node)
