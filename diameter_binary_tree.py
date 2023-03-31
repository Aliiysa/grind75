def diameterOfBinaryTree(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1
        
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0], left + right + 2)

        return 1 + max(right, left)
    
    dfs(root)

    return res[0]
