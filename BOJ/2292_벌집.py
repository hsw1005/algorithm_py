"""
13
""" # -> 3

"""
1 -> 1개
2 3 4 5 6 7 -> 6개
8 9 10 11 12 13 14 15 16 17 18 19 -> 12개
20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 -> 18개
38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 -> 24개
"""

# 내 풀이
# n = int(input())
# arr = [[1]]
# temp = []
# cnt = 1
# for i in range(2, n+1):
#     temp.append(i)
#     if len(temp) == cnt * 6:
#         cnt += 1
#         arr.append(temp)
#         temp = []
#
# arr.append(temp)
# if len(arr[-1]) == 0:
#     arr.pop()
#
# print(len(arr))


# kkjjhhbb 풀이
n = int(input())
i = 0
a = 2
b = 1

while True:
    if n == 1:
        print(1)
        break
    a = a+(6*i)
    b = b+(6*(i+1))
    if a <= n <= b:
        print(i + 2)
        break
    i += 1