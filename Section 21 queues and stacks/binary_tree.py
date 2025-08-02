from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head #root of binary tree

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exists')
            elif new_node.value < current_node.value:
                if current_node.left: #there is a node to the left
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right: #there is a node to the left
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break