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


# class BinaryTree:
#     def __init__(self, root=None):
#         '''
#         :param root: root node of the tree.
#         '''
#         self.root = root


# def insert(root, node):
#     '''
#     :param root: root node of the bst.
#     :param node: node to be inserted in bst.
#     '''
#     if not root:
#         root = node
#         return root
#     else:
#         return insertNode(root, node)


# def insertNode(current, node):
#     '''
#     :param current: current node.
#     :param node: node to be inserted.
#     '''
#     if node.value < current.value:
#         if not current.left:
#             current.left = node
#         else:
#             return insertNode(current.left, node)
#     else:
#         if not current.right:
#             current.right = node
#         else:
#             return insertNode(current.right, node)


# node0 = Node(4)
# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(2)
# node4 = Node(6)

# bst = BinaryTree(node0)

# insert(bst.root, node1)
# insert(bst.root, node2)
# insert(bst.root, node3)
# insert(bst.root, node4)

# print(node0.value)
# print(node0.left.value)
# print(node0.right.value)
