from collections import deque

def rightSideView(root):
    result = []
    q = deque([root])

    while q:
        qLen = len(q)
        rightSide = None

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            result.append(rightSide.val)
    
    return result