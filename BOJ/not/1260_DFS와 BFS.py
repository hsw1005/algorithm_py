n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
graph = [[]]
visited = [False] * (n+1)

for i in range(m):
    arr = list(map(int, input().split()))
    matrix[arr[0]][arr[1]] = 1
    matrix[arr[1]][arr[0]] = 1
    graph.append(arr)

#for i in range(0, len(matrix)):
#    print(matrix[i])

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(v)
print("")
bfs(v)


"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
"""
5 5 3
5 4
5 2
1 2
3 4
3 1
"""