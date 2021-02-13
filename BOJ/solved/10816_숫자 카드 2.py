# 시간 초과 ->
"""
import sys
input = sys.stdin.readline

m = int(input())
deck = list(map(int, input().split()))
n = int(input())
have = list(map(int, input().split()))

answer = []

count = 0
for i in range(n):
    for j in range(m):
        if have[i] == deck[j]:
            count += 1
    answer.append(count)
    count = 0

for i in range(0, len(answer)):
    print(answer[i], end=' ')
"""


# 이건 또 무슨 모듈이람..
from collections import Counter

m = int(input())
deck = list(map(int, input().split()))
n = int(input())
have = list(map(int, input().split()))
deck = Counter(deck)

for i in have:
    print(deck[i], end=" ")

"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""