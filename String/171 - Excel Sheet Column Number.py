class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
            A = 1
            AA = 27

            314 -> 3.100 + 1.10 + 4.1 -> 3.10^2 + 1.10^1 + 4.10^0

            A = 1, B = 2, ...., Z = 26
            AA -> A.26^1 + A.26^0 -> 1.26^1 + 1.26^0 = 27
        '''
        print(ord('A'))
        print(ord('B'))
        print(ord('Z'))
        print(ord('A') - ord('A') + 1)
        print(ord('B') - ord('A') + 1)
        print(ord('C') - ord('A') + 1)
        print(ord('Z') - ord('A') + 1)

        num = 0
        count = len(columnTitle)-1
        for s in columnTitle:
            num += 26**count*(ord(s)-ord('A')+1)
            count -= 1
        return num


ob = Solution()
columnTitle = "ZY"
print(ob.titleToNumber(columnTitle))
