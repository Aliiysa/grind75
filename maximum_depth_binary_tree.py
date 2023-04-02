from collections import deque

class TreeNode:
    def __init__self(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

class Solution:

    def maxDepth1(self, root):  # DFS
        
        # Depth of empty tree is 0
        if not root:
            return 0

        return 1 + max(self.maxDepth1(root.left), self.maxDepth1(root.right))
    
    def maxDepth2(self, root): # BFS

        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def maxDepth2(self, root): # Iterative DFS

        if not root:
            return 0

        stack = [[root, 1]]
        result = 1

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
            
        return result