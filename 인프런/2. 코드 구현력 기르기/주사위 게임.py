"""
3
3 3 6
2 2 2
6 2 5

10000 + n * 1000
1000 + n * 100
n * 100
"""

n = int(input())
arr = []
money = []
result = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.sort()
    arr.append(temp)

for item in arr:
    if item[0] == item[1] == item[2]:
        result = 10000 + item[0] * 1000
    elif item[0] != item[1] == item[2]:
        result = 1000 + item[2] * 100
    elif item[0] == item[1] != item[2]:
        result = 1000 + item[0] * 100
    elif item[0] != item[1] != item[2]:
        result = item[2] * 100

    money.append(result)

print(max(money))


