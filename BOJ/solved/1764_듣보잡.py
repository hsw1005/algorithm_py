"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hear = []
see = []
hear_and_see = []

for i in range(0, n):
    hear.append(input().rstrip('\n'))

for i in range(0, m):
    see.append(input().rstrip('\n'))

count = 0
for i in hear:
    for j in see:
        if i == j:
            hear_and_see.append(i)
            count += 1


hear_and_see.sort(key=lambda x: x[0])

print(count)
for i in range(0, len(hear_and_see)):
    print(hear_and_see[i])
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

hear = []
see = []
hear_and_see = []

for i in range(0, n):
    hear.append(input().rstrip('\n'))

for i in range(0, m):
    see.append(input().rstrip('\n'))

duplicate = list(set(hear) & set(see))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
"""