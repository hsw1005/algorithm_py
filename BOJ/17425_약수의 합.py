# 17425_약수의 합

# 5 -> 1, 2, 10, 70, 10000

n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

sum = 0

answers = []

for number in arr:
    for i in range(1, number+1):
        for j in range(1, i+1):
            if i % j == 0:
                sum += j
            else:
                continue
    answers.append(sum)
    sum = 0

for answer in answers:
    print(answer)

