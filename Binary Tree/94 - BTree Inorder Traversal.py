from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        Time: O(n)
        Space: O(n)
    '''

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return []
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ob = Solution()
print(ob.inorderTraversal(root))
