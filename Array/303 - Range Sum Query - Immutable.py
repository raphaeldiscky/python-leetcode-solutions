from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)
            # print(self.sum)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.sum[right] - self.sum[left - 1]
        else:
            return self.sum[right or left]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(2, 3))
