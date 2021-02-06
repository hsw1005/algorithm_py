zero = [[0] * 19 for i in range(19)]

a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    zero[b-1][c-1] = 1

for i in range(19):
    for j in range(19):
        print(zero[i][j], end=' ')
    print()