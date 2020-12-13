# 단어 정렬

n = int(input())
words = []
for i in range(n):
    words.append(list(map(str, input().split())))
words = set(words)
print(words)


"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""