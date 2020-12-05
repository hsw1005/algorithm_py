str1 = "OOXXOXXOOO"
str2 = "OOXXOOXXOO"
str3 = "OXOXOXOXOXOXOX"
str4 = "OOOOOOOOOO"
str5 = "OOOOXOOOOXOOOOX"
str6 = "XXXXXXXXXXX"

def solution(str):
    temp = str.split("X")               # "X"를 기준으로 자르고, "O"만 남은 배열을 만든다.

    answer = 0
    for i in range(0, len(temp)):
        if len(temp[i]) != 0:       # "X"였던 문자열 부분은 ""으로 남는데, 이는 len("")이 0이다.
            os = len(temp[i])           # "O"들의 길이를 구한다.
            oses = int((os+1)*os / 2)   # 덧셈 시그마 공식. 각 "O"들의 합을 계산한다.
            answer += oses              # "O"들의 총 합을 구한다.
        else:
            pass
    return answer


print(solution(str1))
print(solution(str2))
print(solution(str3))
print(solution(str4))
print(solution(str5))
print(solution(str6))

