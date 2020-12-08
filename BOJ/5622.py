# 다이얼 - Dictionary

dicts = {" ":2,
         "A":3,"B":3,"C":3,
         "D":4,"E":4,"F":4,
         "G":5,"H":5,"I":5,
         "J":6,"K":6,"L":6,
         "M":7,"N":7,"O":7,
         "P":8,"Q":8,"R":8,
         "S":9,"T":9,"U":9,
         "W":10,"X":10,"Y":10,"Z":10,
         "+":11,"-":11,"/":11,"*":11}

str = str(input())

def solution(str):
    answer = 0
    for i in range(0, len(str)):
        alphas = str[i]
        if alphas in dicts.keys():
            answer += dicts[alphas]
            #answer += 1

    print(answer)
solution(str)