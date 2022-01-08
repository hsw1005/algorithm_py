"""
g0en2Ts8eSoft
"""

s = input()
cnt = 0
answer = ""

for i in s:
    if i.isdigit() == True:
        answer += str(i)

answer = int(answer)

for i in range(1, answer+1):
    if answer % i == 0:
        cnt += 1

print(answer)
print(cnt)