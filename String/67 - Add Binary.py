class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            print("carry:", carry)
            result += str(carry % 2)
            print("result:", result)
            carry //= 2
        return result[::-1]


ob = Solution()
a = "11"
b = "10"
print(ob.addBinary(a, b))
