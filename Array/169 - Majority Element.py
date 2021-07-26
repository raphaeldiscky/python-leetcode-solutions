from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            Boyer-Moore Voting Algorithm
            Time: O(n) 
            Space: O(1)
        '''
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


ob1 = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(ob1.majorityElement(nums))
