class Node():
    def __init__(self, data, next_node) -> None:
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    # Adding new data to the end of the queue
    def enqueue(self, data):
        if self.tail is None and self.tail is None:
            self.tail = self.head = Node(data, None)
            return
        
        # adding new data to the tail
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

        return

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next_node

        # For instance, if we have one data
        # and we dequeue the only data
        # so need to set the tail as None
        # that means there will no data at head and tail
        if self.head is None:
            self.tail = None
        return removed