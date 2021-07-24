class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'M': 1000, 'D': 500, 'C': 100,
                  'L': 50, 'X': 10, 'V': 5, 'I': 1}
        prev_value = 0
        sum = 0
        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]
            if int_val < prev_value:
                sum -= int_val
            else:
                sum += int_val
            prev_value = int_val
        return sum


s = "IX"
ob1 = Solution()
print(ob1.romanToInt(s))
