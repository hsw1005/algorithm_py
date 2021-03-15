import random
N = int(input())

arr = []
if N % 2 != 0:
    arr.append(0)

while len(arr) != N:
    number = random.randint(1, 100)
    print(number)
    if number in arr:
        print("hi", number)
        continue
    arr.append(number)
    arr.append(number*(-1))
    arr = list(set(arr))


sum = 0
for i in range(0, len(arr)):
    sum += arr[i]
print(sum)
print(arr)
print(len(arr))