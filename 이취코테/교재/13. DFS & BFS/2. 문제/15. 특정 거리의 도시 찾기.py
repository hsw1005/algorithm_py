n, m, k, x = map(int, input().split())

graph = [[]]
visited = [False] * (n+1)
matrix = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    xy = list(map(int, input().split()))
    graph.append(xy)
    matrix[xy[0]][xy[1]] = 1
print(graph)

for i in range(0, len(matrix)):
    print(matrix[i])

def dfs(v, count):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            count += 1
            if count == k:
                print(i)
            dfs(i, count)

count = 0
dfs(x, count)

"""
4 4 2 1
1 2
1 3
2 3
2 4
"""