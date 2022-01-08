"""
n <= 10,000
m <= 300,000,000
연속된 부분합이 m인 경우의 수.

8 3
1 2 1 3 1 1 1 2
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
total = arr[left]
cnt = 0
while True:
    if total < m:
        if right < n:
            total += arr[right]
            right += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= arr[left]
        left += 1
    else:
        total -= arr[left]
        left += 1

print(cnt)