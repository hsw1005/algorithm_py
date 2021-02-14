n = int(input())
arr = []
for i in range(n):
    xy = list(map(int, input().split()))
    arr.append(xy)

arr.sort(key=lambda arr: (arr[1], arr[0]))

for i in range(0, len(arr)):
    print(arr[i][0], arr[i][1])

"""
5
0 4
1 2
1 -1
2 2
3 3
"""
