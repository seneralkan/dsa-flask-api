class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def to_list(self):
        lst =[]
        if self.head is None:
            return lst
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node

        return lst

    def print_linked_list(self):
        ll_string = ""
        node = self.head
        if node is None:
            print("None--")
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None-"
        print(ll_string)

    def insert_beginnig(self, data):
        """
        This if statement keep record the first node and the last node
        rather than below while loop
        """
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        
        if self.head is None:
            self.insert_beginnig(data)
        
        """
        This code block will always kepp track for last node
        But when we creater a linked list, if we memorize the first head(pointer), we dont need while loop.
        This way will increase complexity.

        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node

            node.next_node = Node(data, None)
            self.last_node = node.next_node

        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node
        """
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None


# ll = LinkedList()
# node4 = Node("data4", None)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)

# ll.head = node1
# ll.print_linked_list()

# ll = LinkedList()
# ll.insert_beginnig("data")
# ll.insert_beginnig("hello")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_beginnig("nerd")
# ll.insert_at_end("end")
# ll.insert_at_end("end2")
# ll.print_linked_list()