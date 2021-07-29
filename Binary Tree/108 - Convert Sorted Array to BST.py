
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        Time: O(n)
        Space: O(n) in the case of skewed binary tree.
    '''

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums) == 0:
            return None
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, low, high):
        if low > high:
            return None
        mid = (low + high)//2
        node = TreeNode(nums[mid])
        # recursively construct the left subtree and make it left child of nums
        node.left = self.helper(nums, low, mid-1)
        # recursively construct the right subtree and make it right child of nums
        node.right = self.helper(nums, mid+1, high)
        return node

    def preOrder(self, node):
        if not node:
            return
        print(node.val, end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)


nums = [-10, -3, 0, 5, 9]
print("original array:", nums)
ob = Solution()
result = ob.sortedArrayToBST(nums)
print("preoder:")
ob.preOrder(result)
