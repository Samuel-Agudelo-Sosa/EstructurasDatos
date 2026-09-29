class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):       
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def generate_hash(self, key):
        return hash(key) % self.capacity
    

    def insert(self, k, v):
        idx = self.generate_hash(k)
        new_node = Node(k, v)
        if self.table[idx] == None:
            self.table[idx] = new_node
            self.size += 1
        else:
            current_node = self.table[idx]
            while current_node.next:
                if current_node.key == k:
                    current_node.value = new_node.value
                    return
                current_node = current_node.next
            if current_node.key == k:
                current_node.value = new_node.value
                return   
            current_node.next = new_node
            self.size += 1
    
    def search(self, k):
        idx = self.generate_hash(k)
        current_node = self.table[idx]
        while current_node:
            if current_node.key == k:
                return current_node.value
            current_node = current_node.next
        return False
    
    def remove(self, k):
        idx = self.generate_hash(k)
        current_node = self.table[idx]
        if current_node is None:
            return False
        if current_node.key == k:
            self.table[idx] = current_node.next
            self.size -= 1
            return True
        while current_node.next:
            if current_node.next.key == k:
                current_node.next = current_node.next.next
                self.size -= 1
                return True
            current_node = current_node.next
        return False


