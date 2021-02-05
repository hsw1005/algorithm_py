s = input()
arr = []
one = 0
zero = 0

for i in range(0, len(s)):
    arr.append(s[i])
    if arr[i] == '1':
        one += 1
    else:
        zero += 1

count = 0

if one > zero:
    for i in range(0, len(arr)-1):
        if arr[i] == '0':
            if arr[i] != arr[i+1]:
                count += 1
    print(count)

elif one < zero:
    for i in range(0, len(arr)-1):
        if arr[i] == '1':
            if arr[i] != arr[i+1]:
                count += 1
    print(count)

else:
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]:
            count += 1
    print(count//2 + 1)


"""
0001100
"""