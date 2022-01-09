"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

"""
#mid와 i의 거리를 활용한다?
n = int(input())
arr = [list(map(int, input().split())) for _ in range()]
mid = n // 2 # mid == 2
answer = 0
for i in range(n):
    for j in range(n):
        if i <= mid:
            for k in range(mid-i, mid+i+1):
                answer += arr[i][k]
        if i > mid:
            #for k in range(n-mid+1, i-mid-1, -1):
            for k in range(i-mid, n-i+mid):
                answer += arr[i][k]
            # if mid <= i+j <= mid*3:
            #     arr[i][j] = 1

print(answer)




""" [i][j] : distance = -2, -1, 0, 1, 2

00 01 __ 03 04  |  __ __ 02 __ __  |  -2  |  0 1 2 3 4
10 __ __ __ 14  |  __ 11 12 13 __  |  -1  |  1 2 3 4 5
__ __ __ __ __  |  20 21 22 23 24  |   0  |  2 3 4 5 6
30 __ __ __ 34  |  __ 31 32 33 __  |   1  |  3 4 5 6 7
40 41 __ 43 44  |  __ __ 42 __ __  |   2  |  4 5 6 7 8

-> 2 | 2 3 4 | 2 3 4 5 6 | 4 5 6 | 6 
"""

