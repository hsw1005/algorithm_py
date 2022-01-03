def solution(number, k):
    answer = ''
    stack = []

    for num in number:
        while stack and stack[-1] < num and k > 0:  # greedy
            stack.pop()
            k -= 1

        stack.append(num)
        # 1. append -> [1]
        # 2. pop, append -> [9]
        # 3. append -> [9, 2]
        # 4. pop, append -> [9, 4]

    # stack에 다 들어갔으나 k가 남아있는 경우.
    if k > 0:
        stack = stack[:-k]

    answer = "".join(stack)
    return answer
