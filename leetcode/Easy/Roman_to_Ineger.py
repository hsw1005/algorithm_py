symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

#alphas = ["I", "V", "X", "L", "C", "D", "M"]
#values = [1, 5, 10, 50, 100, 500, 1000]

# 1
def romanToInt(s):
    sum = 0
    i = 0

    while (i < len(s)):
        if i+1 < len(s) and symbol[s[i]] < symbol[s[i+1]]:
            sum += symbol[s[i+1]] - symbol[s[i]]
            i+=1
            print("1", i, sum)
        else:
            sum+=symbol[s[i]]
        i+=1
        print("2", i, sum)


    return sum


print(romanToInt("LVIII"))

# 2
# 코드 길이 차이봐...비효율의 극치...리스트 생각 그만하기.
def romanToInt(self, s: str) -> int:
    rome_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    s_arr = []
    val_arr = []
    results = []
    sum = 0
    for i in range(0, len(s)):
        s_arr.append(s[i:i + 1])
        val_arr.append(rome_dict.get(s[i:i + 1]))

    # print(val_arr)

    for i in range(0, len(val_arr) - 1):
        if i == 0:
            if (val_arr[i] < val_arr[i + 1]):
                temp = val_arr[i + 1] - val_arr[i]
                results.append(temp)
            if (val_arr[i] > val_arr[i + 1]):
                temp = val_arr[i]
                results.append(temp)
        else:
            if (val_arr[i] < val_arr[i + 1]):
                temp = val_arr[i + 1] - val_arr[i]
                results.append(temp)

    # print(results)

    for i in range(0, len(results)):
        sum = sum + results[i]

    return sum