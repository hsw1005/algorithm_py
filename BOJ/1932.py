import sys
input = sys.stdin.readline

n = int(input())
tri = [[0]*n for i in range(n)]

print(tri)

for i in range(0, n):
    tri[i] = list(map(int, input().split()))

print(tri)