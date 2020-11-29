"""1122. Relative Sort Array https://leetcode.com/problems/relative-sort-array/ """

import time
from typing import List


class Solution:
    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for j in arr2:
            res.extend([j] * arr1.count(j))
            arr1 = list(filter(lambda a: a != j, arr1))
        return res + sorted(arr1)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        indices = {arr2[i]:i for i in range(len(arr2))}
        return sorted(arr1, key= lambda num : indices[num] if num in indices else num + len(arr2))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))

    print("--- %s seconds ---" % (time.time() - start_time))
