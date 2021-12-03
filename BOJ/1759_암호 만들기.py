# 서로 다른 L개의 알파벳, 최소 1개의 모음(a, e, i, o, u), 최소 2개의 자음
# 증가하는 순서, abc -> o  |  bac -> x

n, m = map(int, input().split())
arr = list(map(str, input().split()))

vowel = []
consonant = []
a = [0] * (n+1)
c = [False] * m


def backtrack(idx, n, m):
    if idx == m:
        print("".join(map(str, a)))
        return

    for i in range(1, n+1):
        if c[i]:
            continue

        c[i] = True
        a[idx] = i
        backtrack(idx+1, n, m)
        c[i] = False

backtrack(0, n, m)