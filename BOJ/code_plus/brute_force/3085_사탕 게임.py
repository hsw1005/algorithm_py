"""
3
CCP
CCP
PPC
"""

def check(a):
    n = len(a)
    ans = 1 # 아무것도 연속하지 않으면, 최소값은 1이다.
    for i in range(n):
        cnt = 1
        for j in range(1, n):   # 가로 검사
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

        cnt = 1
        for j in range(1, n):   # 세로 검사
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

    return ans

n = int(input())
a = [list(input()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n: # 오른쪽에 넘치지 않게.
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]

        if i+1 < n: # 아래쪽에 넘치지 않게.
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]

print(ans)
