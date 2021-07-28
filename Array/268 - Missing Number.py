class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ''' HashSet
            Time: O(n)
            Space: O(n)
        '''
        num_set = set(nums)  # 0,1,3
        for i in range(len(nums)):
            if i not in num_set:
                return i

    def missingNumber2(self, nums: list[int]) -> int:
        ''' Bit Manipulation XOR
            Time: O(n)
            Space: O(1)
        '''
        missing = len(nums)
        for i, v in enumerate(nums):
            missing ^= i ^ v
        return missing


ob1 = Solution()
nums = [3, 0, 1]
print(ob1.missingNumber(nums))
print(ob1.missingNumber2(nums))
