from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
            - time complexity O(n+m)
        """
        i1 = m-1
        i2 = n-1
        j = m+n-1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                j -= 1
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                j -= 1
                i2 -= 1
        while i2 >= 0:
            nums1[j] = nums2[i2]
            j -= 1
            i2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
ob1 = Solution()
print(ob1.merge(nums1, m, nums2, n))
