from collections import deque

def countStudents(students, sandwiches):
    q = deque(students)

    sandwiches = sandwiches[:]
    counter = 0

    while q and counter < len(sandwiches):
        if q[0] == sandwiches[0]:
            q.popleft()
            sandwiches.pop(0)
            counter = 0
        else:
            q.append(q.popleft())
            counter += 1
        
    print(len(q))

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
countStudents(students, sandwiches)

