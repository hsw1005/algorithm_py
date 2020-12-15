# 소수 찾기

import sys
input = sys.stdin.readline

n = int(input())

temp = list(map(int, input().split()))

answer = 0
for i in range(n):
    flag = 0
    if temp[i] == 1:
        pass
    else:
        for j in range(1, temp[i]+1):
            if (temp[i] % j == 0):
                flag +=1
        if flag == 2:
            answer+=1
        else:
            continue

print(answer)


"""
4
1 3 5 7
"""

"""
5
2 3 5 6 7
"""

"""
10
1 2 3 4 5 6 7 8 9 10
"""