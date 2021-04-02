from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
oper_num = list(map(int, input().split()))

operations = ["+", "-", "*", "//"]

oper_list = []
for i in range(0, len(oper_num)):
    for j in range(oper_num[i]):
        oper_list.append(operations[i])

perms = list(permutations(oper_list, len(oper_list)))
perms = list(set(perms))

expressions = []

for i in range(0, len(perms)):
    temp = []
    for j in range(0, len(perms[i])):
        temp.append(nums[j])
        temp.append(perms[i][j])
    temp.append(nums[-1])
    #print(temp)
    expressions.append(temp)


if len(expressions) == 1:
    one = map(str, expressions[0])
    two = map(str, expressions[0])
    print(eval("".join(one)))
    print(eval("".join(two)))
else:
    results =[]
    for i in range(0, len(expressions)):
        temp = []
        expression = expressions[i]
        #print(i, "########")
        for j in range(0, len(expressions[i])+1):
            if j % 2 == 0:
                temp.append(str(expression.pop(0)))
                #print("if", temp)
                #print(expression)
            else:
                temp.append(str(expression.pop(0)))
                #print("else", temp)
                #print(expression)
            if len(temp) == 3:
                if temp[1] == "//" and int(temp[0]) < 0:
                    temp[0] = str(abs(int(temp[0])))
                    formula = eval("".join(temp))
                    expression.insert(0, "-"+str(formula))
                    temp = []
                    #print("ex", expression)
                    if len(expression) == 3:
                        expression = map(str, expression)
                        results.append(eval("".join(expression)))
                        break
                else:
                    temp = map(str, temp)
                    formula = eval("".join(temp))
                    expression.insert(0, str(formula))
                    temp = []
                    #print("ex", expression)
                    if len(expression) == 3:
                        expression = map(str, expression)
                        results.append(eval("".join(expression)))
                        break
        results = list(set(results))

    print(max(results))
    print(min(results))


# results = []
# for i in range(0, len(expressions)):
#
#     formula = "".join(expressions[i])
#     result = eval(formula)
#     results.append(result)
#
# print(results)

"""
6
1 2 3 4 5 6
2 1 1 1

return -> 54, -24
"""
"""
2
5 6
0 0 1 0

return -> 30, 30
"""
"""
3
3 4 5
1 0 1 0

return -> 35, 17
"""