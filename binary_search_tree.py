from turtle import right


class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def _insert_recursive(self, value, node):
        if value["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data=value)
            else:
                self._insert_recursive(value=value, node=node.left)
        elif value["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data=value)
            else:
                self._insert_recursive(value=value, node=node.right)
        else:
            return

    def _search_recursive(self, blog_post_id, node):

        if blog_post_id == node.data["id"]:
            return node.data

        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id=blog_post_id, node=node.left)

        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id=blog_post_id, node=node.right)

    def insert(self, value):
        # If there is no root in our BST
        if self.root is None:
            self.root = Node(data=value)
        else:
            self._insert_recursive(value=value, node=self.root)

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False
        return self._search_recursive(blog_post_id, self.root)