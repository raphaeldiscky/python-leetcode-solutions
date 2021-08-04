class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
            O(n)
        '''
        if not root:
            return False

        if root.val == targetSum and not (root.left or root.right):
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # DFS + Stack
    def hasPathSum2(self, root: TreeNode, targetSum: int) -> bool:
        stack = [(root, targetSum)]
        while stack:
            node, _targetSum = stack.pop()
            if node:
                if not node.left and not node.right and node.val == _targetSum:
                    return True
                if node.left:
                    # print("node.left:", node.left.val)
                    # print("ts:", _targetSum-node.val)
                    stack.append((node.left, _targetSum-node.val))
                if node.right:
                    # print("node.rg:", node.right.val)
                    # print("ts:", _targetSum-node.val)
                    stack.append((node.right, _targetSum-node.val))

        return False


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
ob = Solution()
print(ob.hasPathSum(root, 22))
print(ob.hasPathSum2(root, 22))
