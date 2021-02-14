# dfs
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

exit = (n-1, m-1)
print(exit)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True


    return False

for i in range(n):
    for j in range(m):
        dfs(i, j)

for i in range(0, len(graph)):
    print(graph[i])

"""
5 6
101010
111111
000001
111111
111111
"""