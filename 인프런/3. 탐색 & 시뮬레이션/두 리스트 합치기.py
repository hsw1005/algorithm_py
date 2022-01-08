"""
3
1 3 5
5
2 3 6 7 9
"""

n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

answer = narr + marr
answer.sort()

for i in answer:
    print(i, end=" ")