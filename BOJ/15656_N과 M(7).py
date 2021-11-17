n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()
c = [False for _ in range(n+1)]
a = [0] * m

def backtrack(idx, n, m):
    if idx == m:
        print(" ".join(map(str, a)))
        return

    for i in range(0, n):
        c[i] = True
        a[idx] = n_arr[i]
        backtrack(idx+1, n, m)
        c[i] = False

backtrack(0, n, m)