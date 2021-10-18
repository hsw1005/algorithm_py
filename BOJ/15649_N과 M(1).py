from itertools import permutations as perm

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
perms = list(perm(arr, m))

for item in perms:
    for i in range(0, len(item)):
        print(item[i], end=" ")
    print("\n", end="")