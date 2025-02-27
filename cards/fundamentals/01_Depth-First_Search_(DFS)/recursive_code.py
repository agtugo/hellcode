def dfs_recursive(node):
    if not node:
        return
    process(node)
    for child in node.children:
        dfs_recursive(child)