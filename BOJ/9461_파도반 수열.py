# 한단계 성장했다...!

t = int(input())

arr = []
for i in range(t):
    arr.append(int(input()))


p = [1,1,1,2,2]
for i in range(5, 101):
    p.append(p[i-1] + p[i-5])

for i in range(0, len(arr)):
    print(p[arr[i]-1])


# 오늘 저녁 리스트업
# 1. 크라이 치즈 버거
# 2. 한솥도시락
# 3. 멘동
# 4. 아영이네?
# 5. 아까 고깃집 저녁 고기
# 6. 서브웨이
# 7.



"""
2
6
12
"""