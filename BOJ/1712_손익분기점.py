# 손익분기점

import sys
input = sys.stdin.readline

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if c-b<=0:
    print(-1)
else:
    print(int(a/(c-b)+1))