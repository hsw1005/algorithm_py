# 1. 파이썬 자체적으로 제한한 재귀함수 호출수 해제
import sys
sys.setrecursionlimit(100000)

# 2. 행렬의 크기와, 무한대를 표현한 변수 inf 선언.
number = 6
inf = 9999

# 3. 교재에 따른 입력 데이터 행렬 선언.
# 추후 P행렬의 path를 구할 때, 인덱스 오류가 생김으로, 상단과 좌단에 0으로 채운 패딩을 더해준다.
input_array = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, inf, 1, 5],
    [0, 9, 0, 3, 2, inf],
    [0, inf, inf, 0, 4, inf],
    [0, inf, inf, 2, 0, 3],
    [0, 3, inf, inf, inf, 0]
]

# 4. 임의의 자작 데이터 행렬 선언.
hsw_data = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 3, inf, inf, 1],
    [0, 5, 0, inf, inf, 2],
    [0, 6, inf, 0, inf, 2],
    [0, inf, 6, 5, 0, 1],
    [0, inf, inf, 4, 3, 0]
]


# 5. floyd 함수 선언부
def floyd():
    p = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    # 6. 입력 행렬을 변수 d에 대입.
    d = hsw_data

    # 7. k변수는 거쳐가는 노드를 뜻한다.
    for k in range(1, number):
        # 8. i변수는 출발 노드를 뜻한다.
        for i in range(1, number):
            # 9. j변수는 도착 노드를 뜻한다.
            for j in range(1, number):
                # 10. 교재 pseudo-code에 기반한 플로이드 알고리즘 구현.
                if (d[i][k] + d[k][j] < d[i][j]):
                    p[i][j] = k
                    d[i][j] = d[i][k] + d[k][j]


    # 11. D배열을 출력한다.
    print("배열 D ->")
    for i in range(1, number):
        for j in range(1, number):
            print(d[i][j], ' ', end='')
        print('\n')

    # 12. P배열을 출력한다.
    print("배열 P ->")
    for i in range(1, number):
        for j in range(1, number):
            print(p[i][j], ' ', end='')
        print('\n')

    # 13. D배열과 P배열을 리턴한다.
    return d, p

# 14. 교재 pseudo-code에 기반한 path함수 구현.
def path(q, r):
    if p[q][r] != 0:
        path(q, p[q][r])
        print('v', p[q][r])
        path(p[q][r], r)
    else:
        pass

# 15. floyd 함수 호출 및 리턴값 저장.
_, p = floyd()

# 16. path 함수 호출 및 예제에 따른 중간 노드 출력 확인.
path(5, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n20151594")

