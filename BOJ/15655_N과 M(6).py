n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()
c = [False for _ in range(n+1)]
a = [0] * m

def backtrack(start, idx, n, m):
    if idx == m:
        print(" ".join(map(str, a)))
        return

    for i in range(start, n):
        if c[i]:
            continue

        c[i] = True
        a[idx] = n_arr[i]
        backtrack(i+1, idx+1, n, m)
        c[i] = False

backtrack(0, 0, n, m)