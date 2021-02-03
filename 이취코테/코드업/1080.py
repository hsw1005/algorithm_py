n = int(input())
sum = 0
for i in range(1, n+1):
    if sum < n:
        sum += i
        continue
    else:
        print(i-1)
        break


"""
55
"""