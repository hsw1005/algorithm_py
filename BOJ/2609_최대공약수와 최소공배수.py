# 최대공약수와 최소공배수
# 유클리드 호제법

import math

A,B=map(int, input().split())
gcd=math.gcd(A,B)

print(gcd)
print(A*B//gcd)






"""
24 18
"""