# 9012

import sys
input = sys.stdin.readline

n = int(input())
arr = []

left_open = 0
left_close = 0
right_open = 0
right_close = 0

for i in range(n):
    s = input().split()
    arr.append(s[0])

for i in range(0, len(arr)):
    if len(arr[i]) % 2 != 0:
        print("NO")
        continue
    else:
        left = arr[i][:len(arr[i])//2]
        right = arr[i][len(arr[i])//2:]

        for j in range(0, len(left)):
            if left[j] == "(":
                left_open += 1
            elif left[j] == ")":
                left_close += 1
            elif right[j] == "(":
                right_open += 1
            else:
                right_close += 1

            if left_open >= left_close & right_close >= right_open & left_open+right_open == right_open+left_close:
                print("YES")
                break
            else:
                print("NO")
                break




"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""