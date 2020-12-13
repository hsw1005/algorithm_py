# 블랙잭
# brute-force

num, bound = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            if arr[i] + arr[j] + arr[k] > bound:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])

print(result)


"""
5 21
5 6 7 8 9
"""
"""
10 500
93 181 245 214 315 36 185 138 216 295
"""