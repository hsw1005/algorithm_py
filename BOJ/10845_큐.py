# 큐
# 직접 구현 ( class )

import sys
input = sys.stdin.readline


class Queue():
    def __init__(self):
        self.array = []
        self.number = 0

    def push(self, number):
        self.array.append(number)
        print("push : ", self.array)

    def pop(self):
        if len(self.array) == 0:
            #print("-1")
            print("pop : -1")
        else:
            print("pop : ", self.array.pop(0))

    def size(self):
        print("size : ", len(self.array))

    def empty(self):
        if len(self.array) == 0:
            print("empty : 1") # empty
        else:
            print("empty : 0") # full

    def front(self):
        if len(self.array) == 0:
            print("front : -1")
        else:
            print("front : ", self.array[0])

    def back(self):
        if len(self.array) == 0:
            print("back : -1")
        else:
            print("back : ", self.array[-1])



if __name__ == "__main__":
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.front()
    queue.back()
    queue.size()
    queue.empty()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.size()
    queue.empty()
    queue.pop()
    queue.push(3)
    queue.empty()
    queue.front()


"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""