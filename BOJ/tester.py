n = int(input())

s_hour = []
e_hour = []

for i in range(n):
    a, b = input().split("~")
    a = a.strip()
    b = b.strip()
    c, d = a.split(":")
    s_hour.append(int(c+d))
    e, f = b.split(":")
    e_hour.append(int(e+f))


for i in range(0, len(s_hour)):
    for j in range(0, len(e_hour)):
        if s_hour[i] > e_hour[i]:
            print(-1)

start_time = max(s_hour)
end_time = min(e_hour)
s_hour = str(start_time)[:2]
s_min = str(start_time)[2:]
e_hour = str(end_time)[:2]
e_min = str(end_time)[2:]

print(s_hour+":"+s_min+" ~ "+e_hour+":"+e_min)


"""
3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00
"""
"""
4
14:59 ~ 19:00
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 15:59
"""
"""
4
08:00 ~ 11:59
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 15:59
"""