# 9012
num = int(input())

for i in range(num):
    b = input()
    s = list(b)
    sum = 0
    for j in s:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")



"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""
"""
3
((
))
())(()
"""