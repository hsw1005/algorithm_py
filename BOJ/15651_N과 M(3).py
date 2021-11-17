# 메모리 초과..

# from itertools import permutations as perms
#
# n, m = map(int, input().split())
#
# n_arr = [i for i in range(1, n+1) for _ in range(m)]
#
# # n_arr = [i for i in range(1, n+1)]
# perm = list(set(perms(n_arr, m)))
# perm.sort()
#
# for value in perm:
#     for i in value:
#         print(i, end=" ")
#     print()

n, m = map(int, input().split())
n_arr = [0] * m
c = [False for _ in range(n+1)]

def backtrack(idx, start, n, m):
    if idx == m:
        print(" ".join(map(str, n_arr)))
        return

    for i in range(1, n+1):
        c[i] = True
        n_arr[idx] = i
        backtrack(idx+1, start, n, m)
        c[i] = False

backtrack(0, 0, n, m)