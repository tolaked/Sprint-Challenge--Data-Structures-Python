from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            current_node = None
            node = self.storage.head
            while current_node is None and node is not None:
                if node.value == self.current:
                    current_node = node
                node = node.next
            # Edge case for node at tail
            if current_node is self.storage.tail:
                self.storage.delete(self.storage.head)
                self.storage.add_to_head(item)
            else:
                current_node.insert_after(item)
                self.storage.delete(current_node)
        self.current = item

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
