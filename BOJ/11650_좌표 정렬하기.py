# 좌표 정렬하기
# lambda

import sys
input = sys.stdin.readline

n = int(input())

location = []
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    location.append((x, y))

# x좌표 정렬 후
# print(location) -> [(1, 1), (1, -1), (2, 2), (3, 4), (3, 3)]

location.sort(key = lambda x: (x[0], x[1]))

# y좌표 정렬
# print(location) -> [(1, -1), (1, 1), (2, 2), (3, 3), (3, 4)]

for i in range(n):
    print(location[i][0], location[i][1])

"""
5
3 4
1 1
1 -1
2 2
3 3
"""


