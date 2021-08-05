class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        '''
            O(n)
            O(1)
        '''
        if len(nums) < 3:
            return max(nums)

        first = second = third = float('-inf')

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num
            print(first, second, third)

        return third if third != float('-inf') else max(nums)


obj = Solution()
nums = [3, 2, 1]
print(obj.thirdMax(nums))
