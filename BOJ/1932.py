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