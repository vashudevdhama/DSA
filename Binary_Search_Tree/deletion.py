'''
Deletion in Binary Search Tree - Recursive approach
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


def remove(root, value):
    '''
    :root: root node of the bst.
    :value: node value to be deleted.
    '''
    if root is None:
        return root
    elif value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        # Case 1: When no child.
        if root.left is None and root.right is None:
            root = None
        # Case 2: When left child is empty.
        elif root.left is None:
            temp = root
            root = root.right
            temp = None
        # Case 3: When right child is empty.
        elif root.right is None:
            temp = root
            root = root.left
            temp = None
        # Case 4: When both left and right child exists.
        else:
            temp = None
            current = root.right
            while(current.left):
                current = current.left
            temp = current
            root.value = temp.value
            root.right = remove(root.right, temp.value)
    return root
