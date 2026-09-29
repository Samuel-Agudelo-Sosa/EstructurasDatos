class HashTableAbierta:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # Tu tabla guardará tuplas limpias (key, value) directamente en el índice
        self.table = [None] * capacity 
        self.num_deleted = 0


    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        factor_carga = (self.size + self.num_deleted + 1) / self.capacity
        if factor_carga > 0.7:
            self.resize(self.capacity * 2)
        idx = self._hash(key)
        parada = idx
        primer_deleted = None
        
        while True:

            if self.table[idx] is None:
                if primer_deleted is not None:
                    idx = primer_deleted
                    self.num_deleted -= 1
                self.table[idx] = (key, value)
                self.size += 1
                return
            
            elif self.table[idx] == "DELETED":
                if primer_deleted is None:
                    primer_deleted = idx
            
            elif self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            

            idx = (idx + 1) % self.capacity
            

            if idx == parada:
                if primer_deleted is not None:
                    self.table[primer_deleted] = (key, value)
                    self.size += 1
                    return
                raise Exception("HashTable is full")

    
    def search(self, key):
        idx = self._hash(key)
        parada = idx
        while True:
            if self.table[idx] == None:
                return False
            elif self.table[idx] != "DELETED" and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.capacity
            if idx == parada:
                return False
    
        
    def remove(self, key):
        idx = self._hash(key)
        parada = idx
        while True:
            if self.table[idx] == None:
                return False
            elif self.table[idx] != "DELETED" and self.table[idx][0] == key:
                self.table[idx] = "DELETED"
                self.size -= 1
                self.num_deleted += 1
                return True
            idx = (idx + 1) % self.capacity
            if idx == parada:
                return False
            
    def resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.size = 0
        self.num_deleted = 0
        self.table = [None] * new_capacity
        
        for item in old_table:
            if item is not None and item != "DELETED":
                self.insert(item[0], item[1])
    
def encontrar_suma(numeros, objetivo):
    tabla = HashTableAbierta(len(numeros) * 2)
    parejas = set()
    for n in numeros:
        complemento = objetivo - n
        if tabla.search(complemento) is not False:
            parejas.add((min(n, complemento), max(n, complemento)))
        tabla.insert(n, True)
    return parejas if parejas else False
v_num = [8, 7, 2, 5, 3, 1]

print(encontrar_suma(v_num, 10))