"""
5
10 9 10 9 10
7 20
"""

inp_num = int(input())
arr = list(map(int, input().split()))
b, c = list(map(int, input().split()))
cnt = inp_num

for goal in arr:
    if goal - b <= 0:
        continue
    else:
        if goal - b <= c:
            cnt += 1 # 1개의 c로 해결되는 경우.
        else: # goal - b > c
            if (goal - b) % c == 0:
                cnt = cnt + (goal-b)//c
            else:
                cnt = cnt + (goal-b)//c + 1

print(cnt)