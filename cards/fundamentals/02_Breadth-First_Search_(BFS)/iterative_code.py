from collections import deque

def bfs(node):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        process(current)
        queue.extend(current.children)