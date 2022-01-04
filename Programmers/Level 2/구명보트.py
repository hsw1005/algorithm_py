def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    left = 0
    right = len(people) - 1
    weight, boat = 0, 0

    while left != right:
        weight = people[left] + people[right]
        if weight <= limit:  # 가장 무거운 사람 + 가장 가벼운 사람 <= limit
            answer += 1
            left += 1
            right -= 1

        if weight > limit:  # 가장 무거운 사람만 보낸다
            answer += 1
            left += 1

    return answer

print(solution([50, 50, 70, 80], 3))

""" 나의 삽질
def solution(people, limit):
    answer = 0
    boat = 0
    people.sort()
    half = limit // 2

    # 한명만 탈 수 있는 경우.
    for idx, num in enumerate(people):
        if num > half:
            break

    rest = people[:idx]
    answer += len(people) - len(rest)  # 한 명만 탈 수 있는 구명보트 수를 answer에 더함.

    cnt = 0
    for idx, person in enumerate(rest):
        if boat < limit:
            boat += person
            cnt += 1
            if boat >= limit or cnt == 2:
                answer += 1
                boat = 0
                cnt = 0

    if boat != 0 and cnt != 0:
        answer += 1

    return answer
"""