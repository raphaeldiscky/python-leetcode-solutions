class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        print(ord('A'))
        print(chr(66))
        res = ""
        while columnNumber > 0:
            columnNumber -= 1  # 26 -> "Z"
            res += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return res[::-1]


ob = Solution()
columnNumber = 28
print(ob.convertToTitle(columnNumber))
