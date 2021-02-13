z# 나이순 정렬
# lambda

import sys
input = sys.stdin.readline


n = int(input())

temp = []

for i in range(n):
    age, name = map(str, input().split())
    temp.append((int(age), name))

#print(temp) -> [(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]
temp.sort(key=lambda sorted: sorted[0])
#print(temp) -> [(20, 'Sunyoung'), (21, 'Junkyu'), (21, 'Dohyun')]

for sorted in temp:
    print(sorted[0], sorted[1])

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""