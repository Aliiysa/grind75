from collections import deque
def levelOrder(root):
    result = []
    q = deque(root)

    while q:
        level = []
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            result.append(level)
    return result