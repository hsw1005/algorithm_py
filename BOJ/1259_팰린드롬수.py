# 팰린드롬수

n = input()
while n != "0":
    if(n == n[::-1]):
        print('yes')
    else:
        print('no')
    n = input()

"""
121
1231
12421
0
"""