# RGB 거리

import sys
input = sys.stdin.readline

n = int(input())
matrix = [[0]*3 for i in range(n)]
costs = [[0]*3 for i in range(n)]

# 입력
for i in range(0, n):
    matrix[i][0], matrix[i][1], matrix[i][2] = list(map(int, input().split()))

# DP
for i in range(n):
    if i == 0:
        costs[i][0] = matrix[i][0]  # R
        costs[i][1] = matrix[i][1]  # G
        costs[i][2] = matrix[i][2]  # B
    else:
        costs[i][0] = matrix[i][0] + min(costs[i-1][1], costs[i-1][2])
        costs[i][1] = matrix[i][1] + min(costs[i-1][0], costs[i-1][2])
        costs[i][2] = matrix[i][2] + min(costs[i-1][0], costs[i-1][1])

min_cost = min(costs[n-1][0], costs[n-1][1], costs[n-1][2])
print(min_cost)


"""
DP -> 이전 값을 활용하는 방법.

i == 0 일 떄, (첫번째 집을 칠했을 때의 cost 저장.)
matrix = [
    [26, 40, 83],
    [49, 60, 57],
    [13, 89, 99]
]
costs = [
    [26, 40, 83],
    [0, 0, 0],
    [0, 0, 0]
]

i == 1일 때, (두번째 집까지 칠했을 때의 cost 저장.)
costs = [
    [26, 50, 83],
    [89, 86, 83],
    [0, 0, 0]
]

i == 2일 때, (세번째 집까지 칠했을 때의 cost 저장. -> 이 중 최솟값이 최종 결과값.)
costs = [
    [26, 50, 83],
    [89, 86, 83],
    [96, 172, 185]
]

답 -> 96
"""