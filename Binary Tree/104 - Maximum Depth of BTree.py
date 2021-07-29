from collections import deque
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
            A binary tree's maximum depth is the number of nodes along the longest path 
            from the root node down to the farthest leaf node.
        '''
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ob = Solution()
print(ob.maxDepth(root))
