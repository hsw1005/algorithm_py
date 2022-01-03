"""
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
""" # 2

from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, len(arr)):
    for j in range(1, len(arr)):
        power1 = arr[i][j] + arr[j][i]
        print("({0}, {1})".format(i, j), power1)
