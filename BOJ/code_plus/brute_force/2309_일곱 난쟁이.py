"""
20
7
23
19
10
15
25
8
13
"""
from itertools import combinations as comb

arr = []
for _ in range(9):
    arr.append(int(input()))

combs = comb(arr, 7)
combs = list(combs)
for arrs in combs:
    if sum(arrs) == 100:
        answer = arrs
        break

answer = list(answer)
answer.sort()
for item in answer:
    print(item)