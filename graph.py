class Graph:

    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_edge(self, a, b):
        new_edge = (a, b)
        aux = sorted(new_edge)
        new_edge = (aux[0], aux[1])
        self.edges.add(new_edge)

    def count_edges(self, v):
        count = 0
        for e in self.edges:
            if e[0] == v or e[1] == v:
                count += 1
        return count
    
    def get_edges(self, v):
        result = []
        for e in self.edges:
            if e[0] == v or e[1] == v:
                result.append(e);
        return result
