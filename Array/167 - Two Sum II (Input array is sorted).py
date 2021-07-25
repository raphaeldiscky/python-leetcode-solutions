from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            Space: O(n)
            Time: O(n)
        '''
        hash_dict = {}
        for i, val in enumerate(numbers):  # 0 - 4
            complement = target - val
            if complement in hash_dict:
                return [hash_dict[complement]+1, i+1]
            else:
                hash_dict[val] = i


ob1 = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(ob1.twoSum(numbers, target))
