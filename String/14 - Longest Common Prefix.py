from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)  # shortest = "flow"
        for i, ch in enumerate(shortest):
            print('ch:', ch)
            for other in strs:
                print("other["+str(i)+"]:", other[i])
                if other[i] != ch:
                    # return all element except index i --> "fl"
                    return shortest[:i]
        return shortest


strs = ["flower", "flow", "flight"]
ob1 = Solution()
print(ob1.longestCommonPrefix(strs))
