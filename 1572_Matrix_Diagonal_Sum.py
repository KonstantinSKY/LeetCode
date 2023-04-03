"""1572 https://leetcode.com/problems/matrix-diagonal-sum/"""

import time
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        l = len(mat)
        for i in range(l):
            s += mat[i][i] + mat[i][l-i-1] if i != l-i-1 else mat[i][i]
        return s


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print("--- %s seconds ---" % (time.time() - start_time))
