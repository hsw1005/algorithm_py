"""
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
"""


arr = []
card = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0)
for c in card:
    print(c, end=" ")





