"""
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7
"""

sudoku = [list(map(int, input().split())) for _ in range(9)]
answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 0
for i in range(9):
    check_box = []
    check_col = []
    if sudoku[i].sort() == answer:
        cnt += 1
    for j in range(9):
        check_col.append(sudoku[j][i])
        if i % 3 == 1 and j % 3 == 1:
            check_box.append(sudoku[i-1][j-1])
            check_box.append(sudoku[i-1][j])
            check_box.append(sudoku[i-1][j+1])
            check_box.append(sudoku[i][j-1])
            check_box.append(sudoku[i][j])
            check_box.append(sudoku[i][j+1])
            check_box.append(sudoku[i+1][j-1])
            check_box.append(sudoku[i+1][j])
            check_box.append(sudoku[i+1][j+1])
    check_box.sort()
    check_col.sort()

    if check_box == answer or check_col == answer:
        cnt += 1
print(cnt)
print("YES")if cnt == 0 else print("NO")

