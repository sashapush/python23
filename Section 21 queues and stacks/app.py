from node import Node
# #that would be preorder traversal
# left = Node(5)
# head = Node(9)
# right = Node(13)
#
# head.left = left
# head.right = right
#
# print(head)
# print(head.left)
# print(head.right)

#let's see what's binary_tree is
from binary_tree import BinaryTree
tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

print(tree.head)
print(tree.head.left)
print(tree.head.right)