s = input()
num = []
for i in range(0, len(s)):
    num.append(int(s[i]))

#num.sort()

if num[0] == 0:
    result = 0
    plus = num[0] + num[1]
    result += plus

    for i in range(2, len(num)):
            result = result * num[i]
else:
    result = 1
    for i in range(0, len(num)):
        result = result * num[i]

print(result)


"""
02984 -> 576

567   -> 210
"""