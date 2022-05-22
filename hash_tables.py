class Node():
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class Data():
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable():
    def __init__(self, table_size):
        """
        For example: HashTable(4) will return
        [None, None, None, None]
        """
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            # "A" = 65
            # to make that conversion we will use ord()
            """
            The ord() function returns an integer representing the Unicode character.
            """
            hash_value += ord(i)
            # lets give some uniquness to our hash value
            # hash value never exceed the table size
            hash_value = (hash_value * ord(i)) % self.table_size
        
        return hash_value

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            # prevent collison if there same hashed key value
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node

            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            # look next_node is None
            if node.next_node is None:
                return node.data.value
            # look key is equal to one of the other key
            # check and return value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            # look key is equal to selected node
            # so return value
            if key == node.data.key:
                return node.data.value
        # if hash table's key is None
        # return None
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")

# ht = HashTable(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "baby")
# ht.print_table()

"""
{
    [0] None
    [1] hi : there --> hi : there --> hi : there --> hi : baby --> None
    [2] None
    [3] None
}
"""