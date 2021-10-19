"""
6 7 5 1 4 10 2 3 8 9
1 10 2 9 4 8 3 7 5 6
"""

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cnt = 0
b_cnt = 0
l = len(a)
for i in range(0, l):
    if a[i] > b[i]:
        a_cnt += 1
    elif a[i] < b[i]:
        b_cnt += 1
    else:
        continue

if a_cnt > b_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")
else:
    print("D")