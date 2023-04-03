"""832 https://leetcode.com/problems/flipping-an-image/"""

import time
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
        return [[e ^ 1 for e in row] for row in A]

    def flipAndInvertImage1(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                A[i][j] = 1 if A[i][j] == 0 else 0
        return A


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))

    print("--- %s seconds ---" % (time.time() - start_time))
