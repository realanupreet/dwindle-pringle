

def getInOrderTraversal(root):
    #     Write your code here.
    if not root:
        return []
    else:
        return getInOrderTraversal(root.left)+[root.data]+getInOrderTraversal(root.right)
#     pass
