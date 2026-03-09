from collections import deque

class Solution(object):

    def timeRequiredToBuy(tickets, k):
        queue = deque()

        time = 0

        for i, t in enumerate(tickets):
           queue.append((t, i))

        while queue:
            ticket_count, index = queue.popleft()
            ticket_count -= 1

            time += 1

            if ticket_count == 0 and index == k:
                print(time)
                return time
        
            if ticket_count > 0:
                queue.append((ticket_count, index))
        


    tickets = [2, 3, 2]
    k = 2
    timeRequiredToBuy(tickets, k)