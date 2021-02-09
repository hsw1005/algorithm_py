# 0: 북, 1: 동, 2: 남, 3: 서

n, m = map(int, input().split())
r, c, d = map(int, input().split())

matrix = []
global count = 0

for i in range(n):
    matrix.append(list(map(int, input().split())))

robot = matrix[r][c]





"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1
"""

"""
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""