n = int(input())
arr = list(map(int, input().split()))

arr.sort()

target = 1
for coin in arr:
    if target < coin:
        break
    target += coin

print(target)

"""
5
3 2 1 1 9
"""