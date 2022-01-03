"""
N과 M은 4, 6, 8, 12, 20 중 하나.
"""

n, m = map(int, input().split())

nm = [0 for _ in range(n+m)]
total = n * m

for i in range(1, n+1):
    for j in range(1, m+1):
        nm[i+j-1] += 1

max_num = max(nm)

for idx, num in enumerate(nm):
    if num == max_num:
        print(idx+1, end=" ")


