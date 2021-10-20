"""
5 2
1 2 1 1 2
"""
#
# from collections import Counter
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# people = 0
# arr.sort()
#
# counter = Counter(arr)
#
# print(counter.most_common()[0][1])
#

n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = [0 for _ in range(m)]

for i in range(n):
    a[arr[i]-1] += 1

print(max(a))
