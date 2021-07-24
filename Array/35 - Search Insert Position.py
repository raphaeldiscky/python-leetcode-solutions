from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
            - time complexity: O(logn)
            - only work when there is no duplicate
        '''
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def searchInsert_duplicate(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid + 1
            else:
                if target == nums[mid] and nums[mid-1] != target:
                    return mid
                else:
                    high = mid - 1
        return low


nums = [1, 3, 5, 6]
target = 5
ob1 = Solution()
print(ob1.searchInsert(nums, target))
