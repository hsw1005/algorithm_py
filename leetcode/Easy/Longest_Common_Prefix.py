strs = ["flower", "flow", "flight"]

def longestCommonPrefix(strs):
    arrays = []
    answer = []

    for i in range(0, len(strs)):
        arrays.append(list(strs[i]))
    print(arrays)

    for i in range(0, len(arrays)-1):
        if(len(arrays[i]) > len(arrays[i+1])):
            length = len(arrays[i+1])
        else:
            length = len(arrays[i])

    for i in range(0, length):
        for j in range(0, len(arrays)-1):
            prefix = arrays[0][i]
            print(prefix)
            if():
                answer.append(prefix)
            else:
                break
            print(prefix)

    print(answer)
    return answer


longestCommonPrefix(strs)