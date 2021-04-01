# 한단계 성장했다...!

t = int(input())

arr = []
for i in range(t):
    arr.append(int(input()))

p = [1,1,1,2,2]
for i in range(5, 101):
    p.append(p[i-1] + p[i-5])

for i in range(0, len(arr)):
    print(p[arr[i]-1])

"""
2
6
12
"""