"""
4 2
"""
"""
1 2
1 3
1 4
2 3
2 4
3 4
"""

# from itertools import combinations as combs
#
# n, m = map(int, input().split())
# n_arr = [i for i in range(1, n+1)]
# comb = list(combs(n_arr, m))
#
# for value in comb:
#     for i in value:
#         print(i, end=" ")
#     print()

n, m = map(int, input().split())
n_arr = [0] * m
c = [False for _ in range(n+1)]

def backtrack(idx, first, n, m):
    if idx == m:
        print(" ".join(map(str, n_arr)))
        return

    for i in range(first, n+1):
        if c[i]:
            continue
        c[i] = True
        n_arr[idx] = i
        backtrack(idx+1, i+1, n, m)
        c[i] = False

backtrack(0, 1, n, m)