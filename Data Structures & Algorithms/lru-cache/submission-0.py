class Node:
    def __init__(self, key, value):
        # Store the key and value
        self.key = key
        self.value = value

        # Point to neighboring nodes
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # Store the maximum cache size
        self.capacity = capacity

        # Map keys to nodes
        self.cache = {}

        # Create dummy LRU and MRU nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Connect the dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        # Return -1 if the key does not exist
        if key not in self.cache:
            return -1

        # Get the node
        node = self.cache[key]

        # Remove the node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Insert the node at the MRU end
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        # Return the value
        return node.value

    def put(self, key: int, value: int) -> None:
        # Remove the old node if the key already exists
        if key in self.cache:
            old = self.cache[key]
            old.prev.next = old.next
            old.next.prev = old.prev

        # Create and store the new node
        node = Node(key, value)
        self.cache[key] = node

        # Insert the node at the MRU end
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        # Remove the LRU node if over capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next

            # Remove it from the linked list
            self.left.next = lru.next
            lru.next.prev = self.left

            # Remove it from the dictionary
            del self.cache[lru.key]