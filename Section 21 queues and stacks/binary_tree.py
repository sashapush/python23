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
            else: #or elif new_node.value > current_node.value:
                if current_node.right: #there is a node to the left
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f'The given value {value} is not in the tree')

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
        print(current_node)
        self._inorder_recursive(current_node.left)
        self._inorder_recursive(current_node.right)

    #to delete node we need 2 helper methods:
    # Find the parent of a given node
    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            # i.e if left,child node exists and it's equal to the value or
            # if right, child node exists and it's equal to the given value we have a parent node
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value>current_node.value:
                current_node = current_node.right
            elif value<current_node.value:
                current_node = current_node.left


    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
    def delete_node(self, value: int): #https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790270
        #Scenarious are - node with no children, 1 child and 2 children
        #if deleting node with 2 children: Replace the node by the largest node on the left branch OR smallest node in
        # the right branch
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)
        # 2 children are present https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790278#questions
        if to_delete.left and to_delete.right:
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)
            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
            rightmost.right = to_delete.right
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = rightmost
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = rightmost
            else: #deleting the head
                self.head = rightmost
        elif to_delete.left or to_delete.right:
            #1 child
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.right or to_delete.left
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
                self.head = to_delete.right or to_delete.left
        else:
            #No children
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None #parent simply points to None instead of node to delete
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None #parent simply points to None instead of node to delete
            else:
                #only head with no children makes it to this condition
                self.head = None
