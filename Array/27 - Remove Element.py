from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


nums = [3, 2, 2, 3]
val = 3
ob1 = Solution()
print(ob1.removeElement(nums, val))
