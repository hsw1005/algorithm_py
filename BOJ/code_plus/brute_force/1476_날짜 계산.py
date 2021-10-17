e, s, m = map(int, input().split())

our = 1
ee, ss, mm = 1, 1, 1

while True:

    if ee == e and ss == s and mm == m:
        print(our)
        break

    ee += 1
    ss += 1
    mm += 1
    if ee == 16:
        ee = 1
    if ss == 29:
        ss = 1
    if mm == 20:
        mm = 1
    our += 1
