class DisjointSet:
    def __init__(self, elems):
        self.parent = {elem: elem for elem in elems}

    def find_key(self, elem):
        return elem if self.parent[elem] == elem else self.find_key(self.parent[elem])

    def union(self, key1, key2):
        self.parent[key1] = key2
        
