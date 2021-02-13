n, m, k, x = map(int, input().split())

graph = []
matrix = [[0] * n for _ in range(n)]

for i in range(0, m):
    graph.append(list(map(int, input().split())))
    print(graph)

for i in range(0, m):
    matrix[graph[i][0]-1][graph[i][1]-1] = 1

print(graph)
for i in range(0, len(matrix)):
    print(matrix[i])

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n+1)

dfs(graph, x, visited)



"""
4 4 2 1
1 2
1 3
2 3
2 4
"""