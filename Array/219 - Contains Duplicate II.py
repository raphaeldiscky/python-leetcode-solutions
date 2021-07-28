from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
            Time: O(n) using dict
            Space: O(n)
        '''
        dic = {}
        for i, v in enumerate(nums):
            print("i:", i, "v:", v)
            if v in dic and i - dic[v] <= k:  # if v is in same as key in dic
                return True
            dic[v] = i
        return False


ob1 = Solution()
nums = [1, 2, 3, 1]
k = 3
print(ob1.containsNearbyDuplicate(nums, k))
