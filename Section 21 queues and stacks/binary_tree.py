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

    def inordertraversion(self):
        self._inorder_recursive(self.head) #calls another private method (seen by _)
        #so self.head becomes current_node
    def _inorder_recursive(self, current_node: Node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)
        #that's a recursion - when a function or method calls itself

        def _preorder_recursive(self, current_node: Node):
            if not current_node:
                return
            #print(current_node) leaving print here would make this preorder traversal, if print is deleted from L41
            self._inorder_recursive(current_node.left)
            print(current_node)
            self._inorder_recursive(current_node.right)