"""1640. Check Array Formation Through Concatenation https://leetcode.com/problems/check-array-formation-through-concatenation/ """

import time
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for i in pieces:
            if i[0] not in arr:
                return False
            idx = arr.index(i[0])
            for j in range(1, len(i)):
                idx += 1
                print(idx)
                if idx > len(arr)-1:
                    return False
                if i[j] not in arr:
                    return False
                if arr.index(i[j]) != idx:
                    return False
        return True


if __name__ == "__main__":
    start_time = time.time()
    # print(Solution().canFormArray([91, 4, 64, ], [[78], [4, 64], [91]]))
    # print(Solution().canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]))
    # print(Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
    print(Solution().canFormArray([100, 2, 98, 28, 44, 55, 37], [[28, 46, 57], [37, 19, 40, 38]]))

    print("--- %s seconds ---" % (time.time() - start_time))
