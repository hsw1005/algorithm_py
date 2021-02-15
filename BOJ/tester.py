from collections import deque
cmd = deque()
t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    print("a, b, c", a, b, c)
    for i in range(c):
        cmd.append(list(map(int, input().split())))


    print(cmd)
    cmd =[]


"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""