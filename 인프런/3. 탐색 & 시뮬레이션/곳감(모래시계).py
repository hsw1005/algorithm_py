"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
commands = [list(map(int, input().split())) for _ in range(m)]

for command in commands:
    if command[1] == 0: #왼쪽
        for _ in range(command[2]):
            matrix[command[0]-1] = matrix[command[0]-1][1:] + matrix[command[0]-1][:1]
    if command[1] == 1: #오른쪽
        for _ in range(command[2]):
            matrix[command[0]-1] = matrix[command[0]-1][-1:] + matrix[command[0]-1][:-1]

res = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e + 1):
        res += matrix[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)