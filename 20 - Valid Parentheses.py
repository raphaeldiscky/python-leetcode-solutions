class Solution:
    def isValid(self, s: str) -> bool:  # close the last seen opening symbol
        stack = []
        d = {"[": "]", "{": "}",  "(": ")"}

        if not s or len(s) == 0:
            return True

        for ch in s:
            if ch in d.keys():
                stack.append(ch)
            elif len(stack) == 0 or ch != d[stack.pop()]:
                return False
        return len(stack) == 0  # return true if stack empty


s = "([)]"
ob1 = Solution()
print(ob1.isValid(s))
