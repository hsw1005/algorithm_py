import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input()))

maxarr = []
for i in range(1, len(arr)-1):
    maxarr.append(max(arr[i-1]+arr[i+1], arr[i]+arr[i+1]))

print(max(maxarr))

