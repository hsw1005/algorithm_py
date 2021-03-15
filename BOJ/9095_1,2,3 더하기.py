n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

dp = [1, 2, 4] # 초기 1, 2, 3인 경우의 수 넣기
for i in range(3, max(arr)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in arr:
    print(dp[i-1])


"""
3
4
7
10
"""