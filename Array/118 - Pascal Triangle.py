from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
            - Time:
            - Space
        '''
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        triangle = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            print("row: ", row)
            triangle.append(row)
        return triangle


numRows = 5
ob1 = Solution()
print(ob1.generate(numRows))
