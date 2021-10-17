"""
5457
3
6 7 8
"""

input_number = int(input()) # 목표 채널
n = int(input()) # n개
arr = list(map(str, input().split())) # n개만큼 고장난 버튼
all_num = list(str(i) for i in range(10)) # 0~9, +, -
str_num = list(str(input_number)) # 목표 채널을 스트링화
others = [x for x in all_num if x not in arr]

ans = ""
cnt = 0
if input_number == 100:
    print(0)
else:
    for item in str_num:
        if item not in arr:
            ans += item
            cnt += 1
        if item in arr:
            cnt += 1
            for other in others:
                if int(item) < int(other):
                    distance = min(int(other)-int(item), int(others[others.index(other)-1])-int(item))
                    cnt += abs(distance)
    print(cnt)
