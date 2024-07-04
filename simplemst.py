def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_by_size(parent, size, u, v):
    root_u = find_parent(parent, u)
    root_v = find_parent(parent, v)
    
    if root_u != root_v:
        if size[root_u] < size[root_v]:
            parent[root_u] = root_v
            size[root_v] += size[root_u]
        else:
            parent[root_v] = root_u
            size[root_u] += size[root_v]

def spanning_tree(V, adj):
    edges = []
    for i in range(V):
        for it in adj[i]:
            adj_node, wt = it
            edges.append((wt, i, adj_node))
    
    edges.sort()
    
    parent = list(range(V))
    size = [1] * V
    mst_weight = 0
    
    for wt, u, v in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            mst_weight += wt
            union_by_size(parent, size, u, v)
    
    return mst_weight

if __name__ == "__main__":
    V = 5
    edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    mst_weight = spanning_tree(V, adj)
    print("The sum of all the edge weights:", mst_weight)
