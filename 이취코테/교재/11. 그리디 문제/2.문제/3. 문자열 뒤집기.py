s = input()
arr = []
zero = 0
one = 0

if s[0] == '0':
    zero += 1
else:
    one += 1

for i in range(0, len(s)):
    arr.append(s[i])

for i in range(0, len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i] == '0':
            zero += 1
            #print("zero", zero)
        else:
            one += 1
            #print("one", one)
    else:
        continue

print(min(one, zero))



"""
0001100
"""