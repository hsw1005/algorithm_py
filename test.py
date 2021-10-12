from collections import deque

iter = int(input())
round = []
camels = deque()
temp = [[0] for _ in range(iter)]
answer = []


for i in range(iter):
    n = int(input())
    round.append(n)
    camel = list(map(int, input().split()))
    camels.append(camel)

for i in range(iter):
    temp[i].pop(0)
    if len(camels[i]) == 1:
        answer.append(camels[i][0])
        print(answer)
    else:
        time = 0
        while True:
            if len(camels[i]) == 0:
                break

            first = camels[i].pop(0)
            temp[i].append(first)
            second = camels[i].pop(0)
            temp[i].append(second)





'''
2
1
5
4
1 2 8 9
'''