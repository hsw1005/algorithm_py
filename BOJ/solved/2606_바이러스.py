n = int(input())
m = int(input())
visited = [False] * (n+1)

matrix = [[0] * (n+1) for _ in range(n+1)]
graph = [[]]
for i in range(m):
    arr = list(map(int, input().split()))
    graph.append(arr)
    matrix[arr[0]][arr[1]] = 1
    matrix[arr[1]][arr[0]] = 1

def dfs(v):
    visited[v] = True
    #print(v, end=" ")

    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

dfs(1)

count = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        count += 1

print(count-1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

"""
5
5
5 4
5 2
1 2
3 4
3 1
"""
