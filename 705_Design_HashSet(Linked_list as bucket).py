class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket_list = [Bucket() for x in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key: int) -> None:
        self.bucket_list[self._hash(key)].insert(key)

    def remove(self, key: int) -> None:
        self.bucket_list[self._hash(key)].delete(key)

    def contains(self, key: int) -> bool:
        return self.bucket_list[self._hash(key)].exists(key)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            new_node = Node(value)
            new_node.next = self.head.next
            self.head.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False
