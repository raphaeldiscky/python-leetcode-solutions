#  KMP algorithm O(m+n)
class Solution:
    def build_lps(self, needle):
        """ Helper function for strStr.
        Returns longest proper suffix array for string needle.
        Each lps_array[i] is the length of the longest proper prefix
        which is equal to suffix for needle ending at character i.
        Proper means that whole string cannot be prefix or suffix.

        Time complexity: O(m). Space complexity: O(1), where
        m is the length of the needle, space used for lps array isn't included.
        """
        lps_array = [0]*len(needle)  # [0,0,...,n]
        i, j = 1, 0  # start from the 2nd character in needle
        while i < len(needle):
            if needle[i] == needle[j]:
                lps_array[i] = j + 1
                j += 1
                i += 1
            elif j > 0:
                j = lps_array[j-1]
            else:
                lps_array[i] = 0
                i += 1
        return lps_array

    def strStr(self, haystack: str, needle: str) -> int:
        """ Returns index of 1st occurence of needle in haystack.
        Returns -1 if needle is not in the haystack.
        Knuth–Morris–Pratt algorithm.
        Time complexity: O(n + m). Space complexity: O(m).
        """
        # special case
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1

        # build longest proper suffix array for pattern
        lps_array = self.build_lps(needle)
        n, m = len(haystack), len(needle)
        i, j = 0, 0
        while i < n:
            # current character match, move to the next character
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:  # try start with previous longest prefix
                j = lps_array[j-1]
            # 1'st charater of needle doesn't match character in haystack
            # go to next char in haystack
            else:
                i += 1
            # whole needle matches haystack, match is found
            if j == m:
                return i - m

        # no match was found
        return -1


haystack = "aaaaa"
needle = "bba"
ob1 = Solution()
print(ob1.strStr(haystack, needle))
