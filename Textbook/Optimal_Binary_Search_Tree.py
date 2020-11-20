# 20151594 함승우 Optimal Binary Search Tree 과제

# 1. Optimal Binary Search Tree 함수
def OBST(prob):

    n = len(prob)-1

    # 2. 행렬 크기 규정
    A = [[-1] * (n + 1) for _ in range(n + 2)]
    R = [[-1] * (n + 1) for _ in range(n + 2)]

    # 3. 행렬 채우기
    for i in range(1, n+1):
        A[i][i-1] = 0
        A[i][i] = prob[i]
        R[i][i-1] = 0
        R[i][i] = i

    # 4. 대각이 0인 행렬
    A[n+1][n] = 0
    R[n+1][n] = 0

    # 5. Optimal Binary Search Tree 알고리즘
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i+diagonal

            # 6. 최솟값 함수 재귀 호출
            A[i][j], R[i][j] = minimum(A, prob, i, j)

    return A, R


# 7. 최솟값 계산 함수
def minimum(A, p, i, j):

    minValue = INF
    minK = 0

    for k in range(i, j+1):
        value = A[i][k-1] + A[k+1][j]

        for m in range(i, j+1):
            value += p[m]

        if(minValue > value):
            minValue = value
            minK = k

    return minValue, minK

# 8. 입력값 및 변수 선언
INF = 100000

# 8-1. 교재에 따른 입력값 선언
keys = [0, 'Don', 'Isabella', 'Dolph', 'Joan']
# 8-2. 교재에 따른 확률값 선언 -> [3/8, 3/8, 1/8, 1/8]
prob = [0, 0.375, 0.375, 0.125, 0.125]

# 9. 임의의 자작 데이터 선언
hsw_keys = [0, 'Hello', 'my', 'name', 'is', 'Seungwoo']
hsw_prob = [0, 0.2, 0.25, 0.25, 0.2, 0.1]

# 9. 함수 실행 호출
A, R = OBST(prob)

# 10. 출력부
print("\nminAvg -> \n{0}".format(A[1][len(A)-2]))

print('\nA행렬 -> ')
for i in range(1, len(A)):
    print(A[i])

print('\nR행렬 -> ')
for i in range(1, len(R)):
    print(R[i])


if __name__ == "__main__":
    print("\n\n20151594_함승우_OptimalBinarySearchTree")