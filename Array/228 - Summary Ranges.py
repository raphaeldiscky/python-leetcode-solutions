from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
            Time: O(n)
        '''
        if not nums:
            return []
        start, cur, end = nums[0], nums[0], None
        output = []
        for n in nums[1:]:
            print("n:", n, "start: ", start, "cur: ", cur, "end: ", end)
            cur += 1
            if n == cur:
                end = n
            else:
                if not end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = n
                cur = n
                end = None
        if not end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        return output


nums = [0, 2, 3, 4, 6, 8, 9]
ob1 = Solution()
print(ob1.summaryRanges(nums))
