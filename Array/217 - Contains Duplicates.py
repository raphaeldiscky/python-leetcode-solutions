from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
            Time: O(n)
            Space: O(n)
        '''
        dic = {}
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = 1
        return False


ob1 = Solution()
print(ob1.containsDuplicate([1, 2, 3, 1]))
