from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for i in nums1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in nums2:
            if i in dic:
                dic[i] -= 1
                stack.append(i)
            if i in dic and dic[i] == 0:
                del dic[i]
        return stack


obj = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(obj.intersect(nums1, nums2))
