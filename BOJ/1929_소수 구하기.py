# 에라토스 테네스의 체.

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    answer = [i for i in range(2, n+1) if sieve[i] == True]
    return answer


m, n = map(int, input().split())

answer = prime_list(n)

for i in answer:
    if i >= m:
        answer = answer[answer.index(i):]
        break

for i in answer:
    print(i)