from collections import deque

def solution(priorities, location):
    temp = []
    ordered = []

    for i, level in enumerate(priorities):
        temp.append((level, i))

    # print(temp) # 0번 인덱스 : 우선순위, 1번 인덱스 : 인덱스
    # print(max(temp))

    queue = deque(temp)

    while len(queue):
        front = queue.popleft()
        if front[0] == max(temp)[0]:
            ordered.append(front[1])
            temp.remove(max(temp))
        else:
            queue.append(front)

    return ordered.index(location) + 1