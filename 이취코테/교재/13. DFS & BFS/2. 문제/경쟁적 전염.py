n, m = map(int, input().split())

zeroes = [[0] * n for _ in range(m)]
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] != 0:
            virus.append(matrix[i][j])

virus.sort()

def dfs(x, y, vi):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if matrix[x][y] == vi:
        matrix[x][y] = vi
        dfs(x-1, y, vi)
        dfs(x, y-1, vi)
        dfs(x+1, y, vi)
        dfs(x, y+1, vi)
        return True

    return False



result = 0
for i in range(n):
    for j in range(m):
        for vi in virus:
            if dfs(i, j, vi) == True:
                result += 1

print(matrix)
print(matrix[x-1][y-1])
print(result)
"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""