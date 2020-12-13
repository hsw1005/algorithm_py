# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
temp = []
max = 0


for i in range(0, len(arr)-1):
    if(i == 0):
        if(arr[i] < arr[i+1]):
            temp.append(arr[i])
            temp.append(arr[i+1])
        else:
            temp.append(arr[i+1])
            temp.append(arr[i])
    else:
        if(arr[i+1] > arr[i]):
            temp.append(arr[i+1])
        else:
            continue


print(temp)
print(len(temp))
