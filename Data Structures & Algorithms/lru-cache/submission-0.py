class Node:
    def __init__(self, val=0, key=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
class LRUCache:


    def __init__(self, capacity: int):
        self.node_dict = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert_at_right(self, node):

        prev = self.right.prev
        node.prev = prev
        node.next = self.right
        prev.next = node
        self.right.prev = node

    def remove(self, node):

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        node = self.node_dict.get(key)
        if not node:
            return -1

        self.remove(node)
        self.insert_at_right(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.node_dict:
            self.remove(self.node_dict[key])
            del self.node_dict[key]
        node = Node(val =value,key=key)
        self.insert_at_right(node)
        self.node_dict[key] = node

        if len(self.node_dict) > self.capacity:
            lru = self.left.next
            key = lru.key
            self.remove(lru)
            del self.node_dict[key]




        
