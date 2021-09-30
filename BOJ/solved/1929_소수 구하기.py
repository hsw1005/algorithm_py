
import sys
input = sys.stdin.readline

m, n = list(map(int, input().split()))
answer = []

flag = 0
for i in range(m, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            flag += 1

    if flag == 1:
        answer.append(i)
    flag = 0

for num in answer:
    print(num)