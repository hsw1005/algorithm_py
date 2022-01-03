n = int(input())
arr = list(map(int, input().split()))

avg = int(sum(arr)/len(arr) + 0.5)

min = 214700000
score, res = 0, 0
for idx, x in enumerate(arr):
    tmp = abs(avg - x)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)

"""
10
45 73 66 87 92 67 75 79 75 80
"""
