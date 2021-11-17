# from itertools import permutations as perm
#
# n, m = map(int, input().split())
# arr = [i for i in range(1, n+1)]
# perms = list(perm(arr, m))
#
# for item in perms:
#     for i in range(0, len(item)):
#         print(item[i], end=" ")
#     print("\n", end="")

n, m = map(int, input().split())
n_arr = [0] * m
c = [False for _ in range(n+1)]

def backtrack(idx, n, m):
    if idx == m:
        print(" ".join(map(str, n_arr)))
        return

    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        n_arr[idx] = i
        backtrack(idx+1, n, m)
        c[i] = False

backtrack(0, n, m)