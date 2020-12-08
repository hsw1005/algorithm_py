# 정수 삼각형

import sys
input = sys.stdin.readline

# 입력 및 초기화
n = int(input())
tri = [[0]*n for i in range(n)]
answer = []

for i in range(0, n):
    tri[i] = list(map(int, input().split()))

print(tri)
a = tri[0][0]
b = tri[0][0]
c = a
d = b
e = 0
for i in range(0, n+1):
    for j in range(0, i+1):
        print("({0}, {1})".format(i, j))
        a = tri[i][j] + tri[i+1][j]
        b = tri[i][j] + tri[i+1][j+1]

        answer.append(a)
        answer.append(b)

print(answer)

"""
총 4개의 루트 :
(i, j) + (i+1, j) + (i+2, j)
(i, j) + (i+1, j) + (i+2, j+1)
(i, j) + (i+1, j+1) + (i+2, j+1)
(i, j) + (i+1, j+2) + (i+2, j+2)
"""

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""