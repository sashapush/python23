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

# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)

tree.inordertraversion()

print(tree.find(11))
#print(tree.find(12)) raises LookupError since there is no element
######################################
print("New tree block below")
new_tree = BinaryTree(Node(6))
nodes = [5,3,9,7,8,7.5,12,11]
for n in nodes:
    new_tree.add(Node(n))

new_tree.delete_node(9)
new_tree.inordertraversion()