n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

dp = [1, 2, 4] # 초기 1, 2, 3인 경우의 수 넣기
for i in range(3, max(arr)):
    print(str(i-1), dp[i-1], "|", str(i-2), dp[i-2], "|", str(i-3), dp[i-3])
    print("dp", dp)
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    # 입력받은 수까지 1, 2, 3의 합으로 더하면서 모든 경우의 수를 구하고, 해당 인덱스에 접근한걸 print 하는 방식이다.
    # 예를 들어 4까지의 합은, 3까지의 합에 dp[3]을 더하는 것과 같기 때문이다.

for i in arr:
    print(dp[i-1])

"""
[1, 2, 3, 4, 5] ->
[0, 1, 4, 7, 13]
"""
"""
3
4
7
10
"""