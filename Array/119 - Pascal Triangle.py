from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            l = []
            for j in range(i+1):
                if j == 0 or j == i:
                    l.append(1)
                else:
                    l.append(row[j-1] + row[j])
            row = l
            print("row", row)
        return row


ob1 = Solution()
rowIndex = 3
print(ob1.getRow(rowIndex))
