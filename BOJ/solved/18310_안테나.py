# 문제 똑바로 읽기..

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

print(arr[(n-1)//2])

"""
4
5 1 7 9
"""
"""
5
1 3 5 7 9
"""