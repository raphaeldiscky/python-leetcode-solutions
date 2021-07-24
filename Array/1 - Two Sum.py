from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i, val in enumerate(nums):  # 0 - 4
            complement = target - val
            if complement in hash_dict:
                return [hash_dict[complement], i]
            else:
                hash_dict[val] = i


nums = [2, 7, 11, 15]
target = 9
ob1 = Solution()
print(ob1.twoSum(nums, target))
