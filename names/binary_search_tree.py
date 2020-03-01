import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
            # does it have a child to the left?
                # place our new node here
            # otherwise
                # repeat process for the left
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
         if self.value == target:
            return True
         elif target < self.value and self.left:
             return self.left.contains(target)
         elif target > self.value and self.right:
             return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        root = node
        if root:
            self.in_order_print(node.left)
            print(root.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(self)

        while q.len() > 0:
            cur_node = q.dequeue()

            if cur_node.left:
                q.enqueue(cur_node.left)
            if cur_node.right:
                q.enqueue(cur_node.right)

            print(cur_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            current_node = stack.pop()

            if current_node.left:
                    stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
                
            print(current_node.value)
    
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
