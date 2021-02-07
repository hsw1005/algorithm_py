n = int(input())
arr = list(map(int, input().split()))

arr.sort()

group = 0
person = 0

for i in range(0, n):
    fear = arr[i]
    person += 1
    if fear == person:
        group += 1
        person = 0
print(group)


"""
5
2 3 1 2 2
"""