# 정수 삼각형

import sys
input = sys.stdin.readline

# 입력 및 초기화
n = int(input())
tri = [[0]*n for i in range(n)]

for i in range(0, n):
    tri[i] = list(map(int, input().split()))

for i in range(0, n):
    for j in range(0, i):
        pass


"""
총 4개의 루트 :
(i, j) + (i+1, j) + (i+2, j)
(i, j) + (i+1, j) + (i+2, j+1)
(i, j) + (i+1, j+1) + (i+2, j+1)
(i, j) + (i+1, j+2) + (i+2, j+2)
"""