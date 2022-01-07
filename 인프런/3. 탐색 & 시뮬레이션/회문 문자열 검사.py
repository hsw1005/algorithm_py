"""
5
level
moon
abcba
soon
gooG
"""

n = int(input())
arr = list(map(str, input()))
left = 0
right = len(arr)-1

while left != right:
    if arr[left] == arr[right]:
        left += 1
        right -= 1
    else:
