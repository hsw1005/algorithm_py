# 최소 인원수 n = 4, 최소 입학 연도 수 m = 3, 최소 학과 수 k = 3

arrs = ["13123820 BusinessManagement AAA",
       "15047648 Economics AAA",
       "17869244 ComputerScience AAA",
       "19000000 ElectronicEngineering AAA",
       "14281264 Law AAA",
       "19000000 ElectronicEngineering BBB",
       "16188768 BusinessManagement BBB",
       "14634411 ElectronicEngineering BBB",
       "16628760 Economics BBB",
       "14863606 BusinessManagement CCC",
       "13165700 Law CCC",
       "15215218 ComputerScience CCC"]

def solution(arr, n, m, k): # 0 : AAA, 1 : BBB, 2 : CCC
    answer = 0

    clubs = []
    for arr in arrs:
        club = arr.split(" ")[2]
        if club not in clubs:
            clubs.append(club)

    stu_id_list = [[club] for club in clubs]
    class_list = [[club] for club in clubs]
    year_list = [[club] for club in clubs]

    for i, club in enumerate(clubs):
        for arr in arrs:
            stu_id, class_id, stu_club = arr.split(" ")
            year = stu_id[0:2]
            if club == stu_club:
                stu_id_list[i].append(stu_id)
                class_list[i].append(class_id)
                year_list[i].append(year)

    check = [-1, -1, -1]
    commons = []
    for i in range(0, len(stu_id_list)):
        for j in range(i+1, len(stu_id_list)):
            commons.append(list(set(stu_id_list[i]).intersection(stu_id_list[j])))

    for common in commons:
        if len(common) != 0:
            for i in range(0, len(stu_id_list)):
                if common[0] in stu_id_list[i]:
                    idx = stu_id_list[i].index(common[0])
                    stu_id_list[i].pop(idx)
                    class_list[i].pop(idx)
                    year_list[i].pop(idx)
                if len(stu_id_list[i])-1 >= n:
                    check[0] = 1
                if len(list(set(year_list[i])))-1 >= m:
                    check[1] = 1
                if len(list(set(class_list[i])))-1 >= k:
                    check[2] = 1

                if sum(check) == 3:
                    answer += 1
                    break
        else:
            check = [-1, -1, -1]
            continue

    print(answer)
    print(stu_id_list)
    print(class_list)
    print(year_list)

    #list(set(a).intersection(b))


n, m, k = 4, 3, 3
solution(arrs, n, m, k)

