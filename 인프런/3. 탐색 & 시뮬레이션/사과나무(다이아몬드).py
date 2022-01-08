"""
3 <= n <= 20

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid:
            arr[i][j] = 0

