###########################################################################
input = [(1,2),(2,3),(3,2),(2,8),(2,4),(4,6),(1,3)]
print(generate_recommendations(input))

categories where make pairs (2 elements) no two category should be same

Hint: The primary operations are "Find" (to determine which set an element belongs to) and "Union" (to merge two sets). 
Hint: DFS
###########################################################################
# Graph Construction: O(E)
# Connected Components: O(N+E)
# O(N+E+Total Pairs Generated)

from collections import defaultdict

def generate_recommendations(pairs):
    adjacency_list = defaultdict(set)

    for a,b in pairs:
        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    # for product in adjacency_list:
    print(adjacency_list) #  {1: {2, 3}, 2: {8, 1, 3, 4}, 3: {1, 2}, 8: {2}, 4: {2, 6}, 6: {4}}

    def dfs(node, component):
        if node in visited:
            return
        visited.add(node)
        component.add(node)
        for neighbour in adjacency_list[node]:
            dfs(neighbour, component)
            # print()

    visited = set()
    categories = []
    for product in adjacency_list:
        if product not in visited:
            component = set()
            dfs(product, component)
            categories.append(component)

    print("complete")
    print("categories ", categories)

    result = []
    for i in range(len(categories)):
        for j in range(i+1, len(categories)):
            for product1 in categories[i]:
                for product2 in categories[j]:
                    result.append((product1, product2))

    return result


# input = [(1,2),(2,3),(3,2),(2,8),(2,4),(4,6),(1,3)]
input = [(1, 3), (2, 7), (3, 8)]
print(generate_recommendations(input))

###########################################################################
UNION FIND
###########################################################################

# parent # rank

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)} #most likely that many node will have themselves as parent
        self.rank = {i:0 for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def generate_recommendations(pairs):
    all_products = set()
    for a, b in pairs:
        all_products.add(a)
        all_products.add(b)
        
    n = max(all_products) + 1 #0-n labelled products
    uf = UnionFind(n)

    for a, b in pairs:
        uf.union(a, b)

    categories = defaultdict(list)
    print(all_products)
    for product in all_products:
        root = uf.find(product)
        categories[root].append(product)

    return categories


# # input = [(1,2),(2,3),(3,2),(2,8),(2,4),(4,6),(1,3)]
input = [(1, 3), (2, 7), (3, 8)]
print(generate_recommendations(input))
