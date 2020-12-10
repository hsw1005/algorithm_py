# 문자열 반복

n = int(input())
temp = []
for i in range(n):
    temp.append(list(map(str, input().split())))

for i in range(n):
    num, str = int(temp[i][0]), temp[i][1]
    for j in range(0, len(str)):
        print(num*str[j], end="")
    print("\n", end="")