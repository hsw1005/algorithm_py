s = input()
arr = []
for i in range(0, len(s)):
  arr.append(s[i])

number = []
alphabet = []
sum = 0
zero_to_ten = "0123456789"

for i in range(0, len(arr)):
    if arr[i] in zero_to_ten:
        sum += int(arr[i])
    else:
        alphabet.append(arr[i])

alphabet.sort()

print("".join(alphabet)+str(sum))



"""
K1KA5CB7
AJKDLSI412K4JSJ9D
"""