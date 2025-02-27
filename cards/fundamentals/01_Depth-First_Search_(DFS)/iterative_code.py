def dfs(node):
    stack = [node]
    while stack:
        current = stack.pop()
        process(current)
        stack.extend(current.children)