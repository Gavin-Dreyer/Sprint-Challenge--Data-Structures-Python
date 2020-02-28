from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        self.current = self.storage.head
        while self.current:
            list_buffer_contents.append(self.current.value)
            self.current = self.current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
