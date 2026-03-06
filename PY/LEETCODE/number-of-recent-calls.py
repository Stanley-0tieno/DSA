from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        print(self.queue[0])

        while self.queue[0] < t-3000:
            self.queue.popleft()


rc = RecentCounter()

rc.ping(1)
rc.ping(100)
rc.ping(3001)


