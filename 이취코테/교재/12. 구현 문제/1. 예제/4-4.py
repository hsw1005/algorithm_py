n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = []

for i in range(0, n):
    arr.append(list(map(int, input().split())))

# d : 0 = 북, 1 = 동, 2 = 남, 3 = 서
# idx로 접근하기 -> (dx, dy)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
count = 1
is_visited = 0

where = (r, c)
val = arr[r][c]

# checker -> 0, 1을 확인하는 것. -> arr[r][c] 값을 사용.
# character -> 직접 움직이는 것. -> r, c 좌표를 사용.
# move -> 0인 육지를 만나면 정말 움직이도록 하는 것 -> r+dx[d], c+dy[d]를 활용.
# 1. 먼저 checker를 사용한다. 방향을 돌린다는 것은 그냥 반시계 90도가 0인지 1인지 확인한다는 것.
# 2. checker가 0인 경우(1 또는 2가 아닌 경우) 해당 방향으로 move 하고, arr[r][c]를 2로 바꾼다. count에 1을 더한다.
# 3. checker가 0이 아닌 경우, 0인 경우일때까지 회전한다. -> d 값에 1씩 더해주고, 네방향 모두 0이 아닐 경우를 파악하기 위해 flag를 쓴다.
# 4. flag == 3인 경우, 방향을 유지하고 한 칸 뒤로 간다. -> 북: (1, 0) 동: (0, -1) 남: (-1, 0) 서: (0, 1)를 더한다.
# 5. 이렇게 더한 북, 동, 남, 서가 1인 경우 즉, 바다인 경우 움직임을 멈춘다.


def checker(r, c, d):
    if arr[r+dx[d]][c+dy[d]] == 0:  # 0(육지)라면,
        return True
    else:                           # 1(바다) 또는 2(이미 방문) 이라면,
        return False

arr[r][c] = 2
while True:
    flag = checker(r, c, d)
    if flag:
        r = r+dx[d]
        c = c+dy[d]
        where = (r, c)
        print(where)
        arr[r][c] = 2
        count += 1
    else:
        d += 1
        d = d % 4
        is_visited += 1


for i in range(0, len(arr)):
    print(arr[i])

print(count)

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
"""
5 5
2 3 0
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 0 1
1 1 1 1 1
"""
"""
11 10
5 3 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""