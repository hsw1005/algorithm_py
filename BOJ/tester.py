import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(0, len(arr)):
    print(arr[i])

"""
5
5
4
3
2
1
"""