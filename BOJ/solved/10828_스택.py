# 스택
# 직접 구현 ( class )

class Stack():
    def __init__(self):
        self.arr = []
        self.number = 0

    def push(self, number):
        self.arr.append(number)
        print("push : ", self.arr)

    def pop(self):
        if len(self.arr) == 0:
            print("pop : -1")
        else:
            print("pop : ", self.arr.pop(-1))

    def size(self):
        print("size : ", len(self.arr))

    def empty(self):
        if len(self.arr) == 0:
            print("empty : 1")
        else:
            print("empty : 0")

    def top(self):
        if len(self.arr) == 0:
            print("top : -1")
        else:
            print("top : ", self.arr[-1])


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.top()
    stack.size()
    stack.empty()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.size()
    stack.empty()
    stack.pop()
    stack.push(3)
    stack.empty()
    stack.top()


"""
14
push 1
push 2
top
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
top
"""

"""
7
pop
top
push 123
top
pop
top
pop
"""