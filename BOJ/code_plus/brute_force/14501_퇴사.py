# dp[N] = N일까지 얻는 이익.

n = int(input())
time = [0 for i in range(n+1)]
price = [0 for i in range(n+1)]

for i in range(n):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

# 최댓값 저장
dp = [0 for i in range(n+1)]
l = len(time)

for i in range(l-2, -1, -1):
    if time[i]+i <= n: # 날짜 초과 X
        dp[i] = max(price[i] + dp[i+time[i]], dp[i+1])
    else: # 날짜 초과 O
        dp[i] = dp[i+1]

print(dp[0])

"""
t : 3  | 5        | 1  | 1  | 2  | 4  | 2
p : 10 | 20       | 10 | 20 | 15 | 40 | 200
dp: 45 | 20 or 45 | 45 | 35 | 15 | 0  | 0
"""