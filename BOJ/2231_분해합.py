n = int(input())
answer = 0
for i in range(1, n+1):
    arr = list(map(int, str(i)))
    #print(arr)
    result = i + sum(arr)
    if result == n:
        print(i)
        break

    if i == n:
        print(0)

"""
216
"""