def lowestCommonAncestor(root, p, q):

    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA)
     node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes 
    p and q as the lowest node in T that has both p and q as descendants
    (where we allow a node to be a descendant of itself).”
    """

    curr = root

    while curr:
        if (p.val > curr.val) and (q.val > curr.val):
            curr = curr.right
        elif (p.val < curr.val) and (q.val < curr.val):
            curr = curr.left
        else:
            return curr