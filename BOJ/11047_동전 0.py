n, k = map(int, input().split())
pocket = []
count = 0

for i in range(n):
    money = int(input())
    if money > k:
        continue
    else:
        pocket.append(money)

pocket = sorted(pocket, key=lambda x: -x)

for i in range(0, len(pocket)):
    if k != 0:
        count += k // pocket[i]
        k = k % pocket[i]
        if k < pocket[i]:
            pass
    else:
        break

print(count)



"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""

"""
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""

"""
10 11000
1
5
10
50
100
500
1000
5000
10000
50000
"""