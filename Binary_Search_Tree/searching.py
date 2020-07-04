'''
Searching for some value in BST.
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


def bstSearch(root: Node, value):
    '''
    :param root: root node of the tree.
    :param value: value to be searched in bst.
    :rtype: boolean
    '''
    if not root:
        return False
    if root.value == value:
        return True
    elif root.value < value:
        return bstSearch(root.right, value)
    else:
        return bstSearch(root.left, value)
