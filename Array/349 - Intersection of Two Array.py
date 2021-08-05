from typing import List


class Solution:
    '''
        T: O(n+m)
        S: O(n+m)
    '''

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set1, set2)

    # using dict
    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums1:
            d[n] = 1
            print(d)

        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
obj = Solution()
print(obj.intersection(nums1, nums2))
print(obj.intersection2(nums1, nums2))
