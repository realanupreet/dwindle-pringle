# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        level = 0

        def levely(root, level):
            ans.append([])
            ans[level].append(root.val)
            level += 1
            if root.right and root.left:
                ans.append([])
                ans[level].append(root.left.val)
                ans[level].append(root.right.val)
                nl = level+1
                # print(ans)
                levely(root.left, nl)
                levely(root.right, nl)
            elif root.left:
                ans.append([])
                ans[level].append(root.left.val)
                nl = level+1
                # print(ans)
                levely(root.left, nl)
            elif root.right:
                ans.append([])
                ans[level].append(root.right.val)
                nl = level+1
                # print(ans)
                levely(root.right, nl)
            else:
                return
        levely(root, level)
        # print("ans is",ans)
        nmap = {}
        for a in ans:
            if a != []:
                if tuple(a) not in nmap:
                    nmap[tuple(a)] = 1
        ans = list(list(k) for k in nmap.keys())
        # ans.pop([])
        rans = []
        for a in ans:
            rans.append(a[0])
        # print()
        # print("nans is",ans)
        # print("rans is",rans)
        return rans
