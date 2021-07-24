from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            - use kadane's algorithm
            - time complexity O(n)
        '''
        maxSoFar = nums[0]
        maxEndingHere = nums[0]

        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ob1 = Solution()
print(ob1.maxSubArray(nums))
