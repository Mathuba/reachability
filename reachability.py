#Uses python3

import sys

def add_edge(graph, vertex1, vertex2):
    edges = (vertex1, vertex2)
    (v1, v2) = (edges)
    if v1 in graph:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
            graph[v2].append(v1)
    else:
        graph[v1] = [v2]

def reach(adj, x, y):
    #write your code here
    return 0

if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}

    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)
    
    start_vert, end_vert = map(int, sys.stdin.readline().split())
    print("start_vert: ", start_vert)
    print("end_vert: ", end_vert)
    print(graph)

    # print(reach(adj, x, y))
