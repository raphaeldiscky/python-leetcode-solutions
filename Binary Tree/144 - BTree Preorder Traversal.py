from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

    # iterative, stack LIFO
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ob = Solution()
print(ob.preorderTraversal(root))
print(ob.preorderTraversal2(root))
