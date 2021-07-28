from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
            Time: O(n)
            Space: O(1)
        """
        c = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[c], nums[i] = nums[i], nums[c]
                c += 1
        return nums


ob1 = Solution()
nums = [0, 1, 0, 3, 12]
print(ob1.moveZeroes(nums))
