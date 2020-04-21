def rangeSumBST(root, L, R):
    result = 0
    if root == None:
        return result

    if L <= root.val <= R:
        result += root.val

    result += rangeSumBST(root.left, L, R)
    result += rangeSumBST(root.right, L, R)

    return result