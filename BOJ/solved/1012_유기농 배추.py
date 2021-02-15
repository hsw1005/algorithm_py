import sys
sys.setrecursionlimit(10000)

t = int(input())
answer = []
for _ in  range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]

    for i in range(0, k):
        temp = list(map(int, input().split()))
        matrix[temp[1]][temp[0]] = 1

    def dfs(x, y):
        if x<=-1 or x>=n or y<=-1 or y>=m:
            return False

        if matrix[x][y] == 1:
            matrix[x][y] = 2
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True

        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result +=1

    answer.append(result)
    continue

for i in range(0, len(answer)):
    print(answer[i])



"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""
"""
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
"""