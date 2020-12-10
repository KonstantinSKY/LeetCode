"""1619. Mean of Array After Removing Some Elements https://leetcode.com/problems/mean-of-array-after-removing-some-elements/ """

import time
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:

        len_ = len(arr)
        num = len_ // 20
        arr.sort()
        if num > 0:
            arr = arr[num:len_ - num]
            return sum(arr) / len(arr)
        else:
            return sum(arr) / len_


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().trimMean([1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
    print(Solution().trimMean([6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]))
    print(Solution().trimMean(
        [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10,
         8, 2, 3, 4]))
    print(Solution().trimMean(
        [9, 7, 8, 7, 7, 8, 4, 4, 6, 8, 8, 7, 6, 8, 8, 9, 2, 6, 0, 0, 1, 10, 8, 6, 3, 3, 5, 1, 10, 9, 0, 7, 10, 0, 10, 4,
         1, 10, 6, 9, 3, 6, 0, 0, 2, 7, 0, 6, 7, 2, 9, 7, 7, 3, 0, 1, 6, 1, 10, 3]))
    print(Solution().trimMean(
        [4, 8, 4, 10, 0, 7, 1, 3, 7, 8, 8, 3, 4, 1, 6, 2, 1, 1, 8, 0, 9, 8, 0, 3, 9, 10, 3, 10, 1, 10, 7, 3, 2, 1, 4, 9,
         10, 7, 6, 4, 0, 8, 5, 1, 2, 1, 6, 2, 5, 0, 7, 10, 9, 10, 3, 7, 10, 5, 8, 5, 7, 6, 7, 6, 10, 9, 5, 10, 5, 5, 7,
         2, 10, 7, 7, 8, 2, 0, 1, 1]))

    print("--- %s seconds ---" % (time.time() - start_time))
