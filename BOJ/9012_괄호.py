# 9012

import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(input().split())

print(arr)


for i in range(n):
    temp = "".join(arr[i])
    print(temp)

"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""