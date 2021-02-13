# 검증수

temp = input().split()
sum = 0
for i in range(0, len(temp)):
    sum += int(temp[i])**2

print(sum % 10)