from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
            using cyclic sort
            if nums[i] != i+1 and nums[i] != nums[nums[i]-1] then swap nums[i] with nums[i-1]
            O(n)
            O(1)
        '''
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
            print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i+1)
        return res


obj = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(obj.findDisappearedNumbers(nums))
