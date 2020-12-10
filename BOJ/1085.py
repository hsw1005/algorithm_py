# 직사각형에서 탈출

arr = list(map(int, input().split()))
print(min(arr[0], arr[1], arr[2]-arr[0], arr[3]-arr[1]))


"""
x = arr[0]
y = arr[1]
w = arr[2]
h = arr[3]

print(min(x, y, w-x, h-y))
"""

"""
6 2 10 3
"""