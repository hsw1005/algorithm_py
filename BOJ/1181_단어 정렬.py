# 단어 정렬

n = int(input())
words = []
sorted = []

for i in range(n):
    words.append(input())

words = list(set(words))

for word in words:
    sorted.append((len(word), word))

sorted.sort()

for _, word in sorted:
    print(word)



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

