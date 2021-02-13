n, x = input().split()
n = int(n)
x = int(x)

temp = input().split()
answer = []
for i in range(n):
    if int(temp[i]) < x:
        print(temp[i], end=" ")
