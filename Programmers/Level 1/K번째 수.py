def solution(array, commands):
    answer = []

    while len(commands) != 0:
        arr = array
        command = commands.pop(0)
        short_arr = arr[command[0]-1:command[1]]
        short_arr.sort()
        number = short_arr[command[2] - 1]
        answer.append(number)

    return answer