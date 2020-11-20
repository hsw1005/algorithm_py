import sys
# 0. Python 재귀 제한 해제 코드
sys.setrecursionlimit(10000)

# 1. p배열 선언
p = []

# 2. Matrix Chain Multiplication 함수 선언
def MatrixChainAlgo(n, d, p):

    # 3. m배열 및 p배열 n의 크기만큼 설정
    m = [[0 for x in range(n)] for x in range(n)]
    p = [[0 for x in range(n)] for x in range(n)]

    # 4. m배열, p배열 0으로 초기화
    for i in range(1, n):
        m[i][i] = 0
        p[i][i] = 0

    # 5. Matrix Chain Multiplication 실행
    for diagonal in range(2, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal - 1
            m[i][j] = sys.maxsize
            p[i][j] = sys.maxsize

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + d[i - 1] * d[k] * d[j]

                # 6. 최소치의 cost와 k값을 저장
                if cost < m[i][j]:
                    m[i][j] = cost
                    p[i][j] = k

    # 7. m배열 출력
    print("\nM 배열 > ")
    for idx in range(0, len(m)):
        print(m[idx])

    # 8. p배열 출력
    print("\nP 배열 > ")
    for idx in range(0, len(p)):
        print(p[idx])

    # 9. Print Optimal Order 실행 및 출력
    print("\nPrint Optimal Order > ")
    order(p, i, j)

    return m[1][n - 1]

# 10. Print Optimal Order 선언부
def order(p, i, j):
    if(i == j):
        print(" A{0} ".format(i), end="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p, i, k)
        order(p, k+1, j)
        print(")", end="")

# 11. 교재 예제 데이터 입력
example_arr = [5, 2, 3, 4, 6, 7, 8]
example_size = len(example_arr)
# arr는 아래 여러 행렬의 크기와 같음
# -> a1 = (5x2) / a2 = (2x3) / a3 = (3x4) / a4 = (4x6) / a5 = (6x7) / a6 = (7x8)

# 12. 자작 데이터 입력
hsw_arr = [3, 5, 2, 6, 8, 2, 3]
hsw_size = len(hsw_arr)
# hsw_arr는 아래 여러 행렬의 크기와 같음.
# -> a1 = (3x5) / a2 = (5x2) / a3 = (2x6) / a4 = (6x8) / a5 = (8x2) / a6 = (2x3)

# 13. 함수 최초 call
print("\n\n곱셈의 최솟 값은 " +
      str(MatrixChainAlgo(example_size, example_arr, p)))

if __name__ == '__main__':
    print("\n20151594 Chained Matrix algorithm")
