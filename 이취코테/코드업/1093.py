a=int(input())
b=input().split()

arr=[]

for i in range(24):
    arr.append(0)
for i in range(a):
    arr[int(b[i])]+=1

for i in range(1, 24):
    print(arr[i], end=' ')
