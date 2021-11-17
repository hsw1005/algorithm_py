
n, m = map(int, input().split())
n_arr = [0] * m
c = [False for _ in range(n+1)]

def backtrack(idx, start, n, m):
    if idx == m:
        print(" ".join(map(str, n_arr)))
        return

    for i in range(start, n+1):
        c[i] = True
        n_arr[idx] = i
        backtrack(idx+1, i, n, m)
        c[i] = False

backtrack(0, 1, n, m)
