from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 0
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]

        return count + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
ob1 = Solution()
print(ob1.removeDuplicates(nums))
