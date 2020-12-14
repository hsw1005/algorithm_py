# 나이순 정렬

n = int(input())

temp = []

for i in range(n):
    age, name = input().split()
    temp.append(list(int(age), name))

sorted = []

temp.sort()

for i in range(n):
    print(temp[i])

"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""