from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Bitwise XOR
            Time: O(n)
            Space: O(1)
        '''
        a = 0
        for i in nums:
            a ^= i
        return a

    def singleNumber2(self, nums: List[int]) -> int:
        '''
        hash table
            Time: O(n)
            Space: O(n)
        '''
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
                print(hash_map)
            else:
                hash_map[i] += 1
                print(hash_map)

        for k, v in hash_map.items():
            if v == 1:
                return k


ob1 = Solution()
nums = [2, 2, 1]
print(ob1.singleNumber(nums))
print(ob1.singleNumber2(nums))
