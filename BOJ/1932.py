# 정수 삼각형

import sys
input = sys.stdin.readline

# 입력 및 초기화
n = int(input())
tri = []
answer = []

for i in range(0, n):
    tri.append(list(map(int, input().split())))

#print(tri)

k = 2

for i in range(1, n):
    for j in range(k):
        if j == 0:
            tri[i][j] = tri[i][j] + tri[i-1][j]
        elif j == i:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])
    k += 1

print(max(tri[n-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""