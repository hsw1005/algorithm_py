"""
4
10 8 5 7 9
10 9 10 9 5
10 3 5 9 10
1 2 3 6 9
"""

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for a in arr:
    a.pop(a.index(max(a)))
    a.pop(a.index(min(a)))
    max_num = max(a)
    min_num = min(a)
    if max_num - min_num >= 4:
        print("KIN")
    elif max_num - min_num < 4:
        print(sum(a))