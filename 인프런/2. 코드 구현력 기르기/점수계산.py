"""
10
1 0 1 1 1 0 0 1 1 0
"""

n = int(input())
arr = list(map(str, input().split()))
arr = "".join(arr).split("0")
answer = 0

for one in arr:
    if one != '':
        l = len(one)
        answer += sum([i for i in range(1, l+1)])

print(answer)