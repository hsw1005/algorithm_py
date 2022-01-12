"""
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2

-> 10
"""

n = int(input())
arr = []
zeros = [0] * (n+2)
arr.append(zeros)
for _ in range(n):
    inp = list(map(int, input().split()))
    inp.insert(0, 0)
    inp.append(0)
    arr.append(inp)
arr.append(zeros)

answer = 0

for i in range(1, len(arr)-1):
    for j in range(1, len(arr)-1):
        if arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i][j-1]:
            answer += 1
        else:
            continue

print(answer)