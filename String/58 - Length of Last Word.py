class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordlist = s.split()
        print(wordlist)
        if wordlist:
            return len(wordlist[-1])
        return 0

    def lengthOfLastWord2(self, s: str) -> int:
        lenLast = 0
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            if s[i] != ' ':
                lenLast += 1
            elif lenLast > 0:
                break
        return lenLast


ob1 = Solution()
s = "hello world i'm your god"
print(ob1.lengthOfLastWord(s))
print(ob1.lengthOfLastWord2(s))
