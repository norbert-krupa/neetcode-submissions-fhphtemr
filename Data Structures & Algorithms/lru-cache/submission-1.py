class LRUCache:

    class KeyNode:
        def __init__(self, key:int, value: int):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    def __init__(self, capacity: int):

        self.max_capacity = capacity
        self.cache = {}

        self.head = self.KeyNode(0, 0)
        self.tail = self.KeyNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def _add_node_to_head(self, node: KeyNode):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node
    
    def _remove_node(self, node: KeyNode):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def _remove_tail(self) -> int:
        node = self.tail.prev
        self._remove_node(node)
        return node.key
    
    def _move_node_to_head(self, node: KeyNode):
        self._remove_node(node)
        self._add_node_to_head(node)
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self._move_node_to_head(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._move_node_to_head(self.cache[key])
            self.cache[key].value = value
        else:
            if len(self.cache) + 1 > self.max_capacity:
                removed_key = self._remove_tail()
                del self.cache[removed_key]
            
            new_node = self.KeyNode(key, value)
            self._add_node_to_head(new_node)
            self.cache[key] = new_node