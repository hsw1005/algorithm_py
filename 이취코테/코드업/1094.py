arr=[]

a=int(input())
b=input().split()

for i in range(a) :
    arr.append(int(b[i]))

i=a-1
while i>=0 :
    print(arr[i], end=' ')
    i-=1