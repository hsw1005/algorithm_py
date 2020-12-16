# 덱
# 직접 구현 ( class )

class Deque():
    def __init__(self):
        self.arr = []
        self.number = 0

    def push_front(self, number):
        self.arr.insert(0, number)
        print("push_front : ", self.arr)

    def push_back(self, number):
        self.arr.append(number)
        print("push_back : ", self.arr)

    def pop_front(self):
        if len(self.arr) == 0:
            print("pop_front : -1")
        else:
            print("pop_front : ", self.arr[0])
            self.arr.pop(0)

    def pop_back(self):
        if len(self.arr) == 0:
            print("pop_back : -1")
        else:
            print("pop_back : ", self.arr[-1])
            self.arr.pop()

    def size(self):
        print("size : ", len(self.arr))


    def empty(self):
        if len(self.arr) == 0:
            print("empty : 1")
        else:
            print("empty : 0")

    def front(self):
        if len(self.arr) == 0:
            print("front : -1")
        else:
            print("front : ", self.arr[0])

    def back(self):
        if len(self.arr) == 0:
            print("back  : -1")
        else:
            print("back : ", self.arr[-1])


if __name__ == "__main__":
    deq = Deque()
    deq.push_back(1)
    deq.push_front(2)
    deq.front()
    deq.back()
    deq.size()
    deq.empty()
    deq.pop_front()
    deq.pop_back()
    deq.pop_front()
    deq.size()
    deq.empty()
    deq.pop_back()
    deq.push_front(3)
    deq.empty()
    deq.front()

