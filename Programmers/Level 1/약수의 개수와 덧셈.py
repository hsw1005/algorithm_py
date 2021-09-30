def solution(left, right):
    arr = []
    count = 0
    for num in range(left, right + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count % 2 == 0:
            arr.append(num)
        else:
            arr.append(-num)
        count = 0

    answer = sum(arr)

    return answer