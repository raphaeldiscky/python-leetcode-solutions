class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Time: O(n)
            Space: O(1)
        '''
        ht = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        for i in t:
            if i in ht:
                ht[i] -= 1
            else:
                ht[i] = 1
        for i in ht:
            if ht[i] != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
ob = Solution()
print(ob.isAnagram(s, t))
