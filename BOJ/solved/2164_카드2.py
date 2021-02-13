# 카드2
# deque

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

cards= []
for i in range(1, n+1):
    cards.append(i)

cards = deque(cards)

for i in range(0, n):
    if len(cards) == 1:
        print(cards[0])
        break
    else:
        cards.popleft()
        cards.append(cards[0])
        cards.popleft()


"""
6
"""