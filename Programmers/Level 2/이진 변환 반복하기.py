def solution(s):
    answer = []
    sum = 0
    phase = 0
    for i in range(10):
        s, count = recursive(s)
        sum += count
        phase += 1
        if(len(s) == 1):
            break

        print(s, count)
        print(sum)
        print('phase', phase)

    answer.append(phase)
    answer.append(count)

    return answer


def recursive(s):
    temp = []
    count = 0
    for i in range(0, len(s)):
        temp.append(s[i])

    for j in range(0, len(temp)):
        if temp[j] == '0':
            del (temp[j])
            count+=1

    return temp, count

s = "110010101001"
answer = solution(s)
print(answer)
print(answer)