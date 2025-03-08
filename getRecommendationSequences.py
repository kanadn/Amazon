MOD = 10**9 + 7

def getRecommendationSequenceCount(category_nodes, k, category_from, category_to, viral_val):
    # Initialize union-find structures.
    parent = list(range(category_nodes))
    size = [1] * category_nodes

    def find(x):
        # Path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        # Union by size: attach the smaller tree to the larger tree.
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

    # Union nodes connected by an edge with viral potential 0.
    for u, v, viral in zip(category_from, category_to, viral_val):
        if viral == 0:
            union(u, v)
    
    # Count sizes for each connected component in the subgraph of 0-edges.
    comp_sizes = {}
    for i in range(category_nodes):
        root = find(i)
        comp_sizes[root] = comp_sizes.get(root, 0) + 1
    
    # Total sequences using all nodes.
    total_sequences = pow(category_nodes, k, MOD)
    
    # Count "bad" sequences: sequences entirely contained in one 0-component.
    bad_sequences = 0
    for comp_size in comp_sizes.values():
        bad_sequences = (bad_sequences + pow(comp_size, k, MOD)) % MOD

    # Valid sequences are those that include at least one viral edge.
    valid_sequences = (total_sequences - bad_sequences) % MOD
    return valid_sequences

# Example usage:
category_nodes = 4
k = 2
category_from = [0, 0, 2]
category_to = [1, 2, 3]
viral_val = [1, 1, 0]

result = getRecommendationSequenceCount(category_nodes, k, category_from, category_to, viral_val)
print("Number of valid recommendation sequences:", result)

category_nodes = 3
k = 3
category_from = [2, 0]
category_to = [1, 1]
viral_val = [1, 1]

result = getRecommendationSequenceCount(category_nodes, k, category_from, category_to, viral_val)
print("Number of valid recommendation sequences:", result)
