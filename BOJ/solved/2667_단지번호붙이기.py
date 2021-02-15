n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

flags = []
flag = 0
def dfs(x, y, flag, flags):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2
        flag += 1
        dfs(x-1, y, flag, flags)
        dfs(x, y-1, flag, flags)
        dfs(x+1, y, flag, flags)
        dfs(x, y+1, flag, flags)
        flags.append(flag)
        return True

    return False

answer = []
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j, flag, flags) == True:
            #flag += 1
            result += 1
            answer.append(len(flags))
        else:
            flag = 0
            flags = []

#for i in range(0, len(graph)):
#    print(graph[i])

print(result)
answer.sort()
for i in range(0, len(answer)):
    print(answer[i])


"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
"""
8
01101000
01101010
11101010
00001110
01000001
01111101
01110001
00001110
"""