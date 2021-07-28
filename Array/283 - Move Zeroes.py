from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
            Time: O(n)
            Space: O(1)
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


ob1 = Solution()
nums = [0, 1, 0, 3, 12]
print(ob1.moveZeroes(nums))
