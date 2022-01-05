"""
5
32 55 62 3700 250
"""

def reverse(num):
    num = int(str(num)[::-1])
    if isPrime(num) == True:
        return num
    else:
        return -1

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    else:
        return True

n = int(input())
arr = list(map(int, input().split()))

for num in arr:
    rev_num = reverse(num)
    if rev_num != -1:
        print(rev_num, end=" ")
    else:
        continue