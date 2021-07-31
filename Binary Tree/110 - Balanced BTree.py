class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    First define a maxDepth dfs helper to quickly get the level of depth of the node.
    Then to check if the following three conditions are all satisfied:
        - check if the root itself is height-balanced (by checking if the absolute difference of the levels of depth between root's left child and right child is less than 2)
        - check if the root's left child is height-balanced (by recursion)
        - check if the root's right child is height-balanced (by recursion)
    '''

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return (abs(l-r) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
ob = Solution()
print(ob.isBalanced(root))
