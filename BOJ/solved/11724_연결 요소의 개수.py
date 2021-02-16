import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
graph = []
for i in range(m):
    temp = list(map(int, input().split()))
    graph.append(temp)
    matrix[temp[0]][temp[1]] = 1
    matrix[temp[1]][temp[0]] = 1

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    #print(v, end=" ")
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

count = 0
for i in range(1, len(visited)):
    if visited[i] == False:
        dfs(i)
        count += 1
    else:
        continue

print(count)


"""
6 5
1 2
2 5
5 1
3 4
4 6
"""
"""
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""