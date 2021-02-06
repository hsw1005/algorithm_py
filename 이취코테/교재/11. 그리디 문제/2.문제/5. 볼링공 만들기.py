n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

for i in range(0, n):
    for j in range(i):
        if arr[i] != arr[j]:
            count += 1

print(count)


"""
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
"""