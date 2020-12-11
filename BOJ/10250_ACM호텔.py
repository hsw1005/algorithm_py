# ACM 호텔
#import numpy as np

n = int(input())
inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

# inputs[x][0] : 층 , inputs[x][1] : 호 , inputs[x][2] : 순서
# 묵을 객실은 순서를 층과 호수로 나눈 나머지와 몫이다.

for idx in range(0, len(inputs)):
    # 꼭대기층인 경우
    if(inputs[idx][2] % inputs[idx][0] == 0):
        floor = inputs[idx][0]
        room_number = inputs[idx][2] // inputs[idx][0]
        # 호수 지정 방식
        if room_number < 10:
            room_number = "0" + str(room_number)
        else:
            room_number = str(room_number)
    else:
        floor = inputs[idx][2] % inputs[idx][0]
        room_number = inputs[idx][2] // inputs[idx][0] + 1
        if room_number < 10:
            room_number = "0" + str(room_number)
        else:
            room_number = str(room_number)
    print(str(floor)+room_number)


"""
2
6 12 10
30 50 72
"""
