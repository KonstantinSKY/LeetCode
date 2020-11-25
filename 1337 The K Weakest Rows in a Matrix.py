"""1337. The K Weakest Rows in a Matrix https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/ """

import time
from typing import List


class Solution:
    def kWeakestRows1(self, mat: List[List[int]], k: int) -> List[int]:
        n = sorted([(mat[i], i) for i in range(len(mat))])
        return [n[i][1] for i in range(k)]

    def kWeakestRows2(self, mat: List[List[int]], k: int) -> List[int]:
        n = sorted([(sum(mat[i]), i) for i in range(len(mat))])
        return [n[i][1] for i in range(k)]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted([i for i in range(len(mat))], key=lambda x: mat[x])[:k]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
                                  3))
    print(Solution().kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2))
    print("--- %s seconds ---" % (time.time() - start_time))
