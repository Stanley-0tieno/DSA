from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A"],
    "D": ["B"],
    "E": ["B"]
}

def bfs(start):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()

        if node not in visited:
            print(node)
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)

bfs("A")