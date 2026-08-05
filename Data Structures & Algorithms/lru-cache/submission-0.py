class Node():
    def __init__(self, val=0, key = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}
        self.head= Node(0)
        self.tail = Node(0)

        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node     

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            newNode = Node(value, key)
            self.keyToNode[key] = newNode
            self.insert(newNode)
            if len(self.keyToNode) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.keyToNode[lru.key]
        
