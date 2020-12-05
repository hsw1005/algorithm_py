from itertools import permutations

list1 = [6, 2, 10]
list2 = [3, 30, 34, 5, 9]

def solution():
    answer = []
    temp = []
    cases = list(permutations(list1, len(list1)))
    cases = list(map(list, cases))
    cases = list(map(str, map(list, cases)))
    print(cases)
    return 0

solution()



"""
map 사용 :
for idx in range(0, len(cases)):sudo a
    cases[idx] = list(cases[idx])
    
-> cases = list(map(list, cases))
"""