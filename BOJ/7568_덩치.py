"""
5
55 185
58 183
88 186
60 175
46 155
""" # -> 2 2 1 2 5

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
cnts = []

for i in range(0, n):
    cnt = 1
    for j in range(0, n):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
    print(cnt, end=" ")
