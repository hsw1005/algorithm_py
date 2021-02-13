# 수 정렬하기2
# sys.stdin / sys.stdout으로 입출력 속도 개선.

import sys
input = sys.stdin.readline
n = int(input())

temp = []
for i in range(n):
    temp.append(int(input()))

for i in sorted(temp):
    sys.stdout.write(str(i)+'\n')


"""
5
5
4
3
2
1
"""