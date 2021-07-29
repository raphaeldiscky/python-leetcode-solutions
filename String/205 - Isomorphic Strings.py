class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
            Time: O(n)
            Space: O(1)
        '''
        mapping_s_t = {}
        mapping_t_s = {}

        for c1, c2 in zip(s, t):
            print(mapping_s_t)
            print(mapping_s_t.get(c1))
            # no mapping exist in either of the dict
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
        return True


ob = Solution()
s = "egg"
t = "add"
print(ob.isIsomorphic(s, t))
