#### UnionFind #####

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        root_set = set(uf.find(i) for i in range(n))
        return len(root_set)


#### DFS #####


from collections import defaultdict

def generate_recommendations(pairs):
    adjacency_list = defaultdict(set)
    for a, b in pairs:
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    print("Adjacency List:", adjacency_list)

    def dfs(node, component):
        if node in visited:
            return
        visited.add(node)
        component.add(node)
        for neighbor in adjacency_list[node]:
            dfs(neighbor, component)

    visited = set()
    categories = []
    for product in adjacency_list:
        if product not in visited:
            component = set()
            dfs(product, component)
            categories.append(component)

    print("Categories:", categories)
    return categories

pairs = [(1, 2), (2, 3), (3, 2), (2, 8), (2, 4), (4, 6), (1, 3)]
categories = generate_recommendations(pairs)
print("Final Categories:", categories)
