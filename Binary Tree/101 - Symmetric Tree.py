class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
            Time: O(n)
            Space: O(n)
        '''
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.right.left = TreeNode(4)

ob = Solution()
print(ob.isSymmetric(root))
