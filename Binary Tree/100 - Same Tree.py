class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
            Time: O(n)
            Space: O(logn)
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def dfs_stack(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(5)

ob = Solution()
print(ob.isSameTree(root1, root2))
print(ob.dfs_stack(root1, root2))
