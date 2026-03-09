from collections import deque

class MovingAvarages:

    def __init__(self, size):
        self.q = deque()
        self.size = size
        self.total = 0

    def next(self, val):
        self.q.append(val)
        self.total += val

        if len(self.q) > self.size:
            removed = self.q.popleft()
            self.total -= removed

        print(self.total/ len(self.q))
mv = MovingAvarages(3)

mv.next(10)
mv.next(20)
mv.next(40)



