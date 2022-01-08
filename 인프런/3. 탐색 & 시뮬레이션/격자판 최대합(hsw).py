"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
# matrix = [list(map(int, input().split())) for _ in range(n)]


temp = 0
rows = []
# row 합
for i in range(0, len(matrix)-1):
    best_row = max(sum(matrix[i]), sum(matrix[i+1]))
    rows.append(best_row)

best_row = max(rows)

# col 합
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    # 왜 'ret = [[0] * N] * N'과 같이 하지 않는지 헷갈리시면 연락주세요.

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

cols = []
matrix2 = rotate_90(matrix)
for i in range(0, len(matrix2)-1):
    best_col = max(sum(matrix2[i]), sum(matrix2[i+1]))
    cols.append(best_col)

best_col = max(cols)

# diagonal
right_diag = 0
left_diag = 0
for i in range(0, len(matrix)):
    for j in range(i, len(matrix)):
        if i == j:
            left_diag += matrix[i][j]

for i in range(len(matrix)-1, 0, -1):
    for j in range(i, len(matrix)):
        if i == j:
            right_diag += matrix[i][j]

print(max(best_row, best_col, left_diag, right_diag))
