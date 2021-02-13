k = int(input())

arr = []

for i in range(0, k):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))

"""
4
3
0
4
0
"""