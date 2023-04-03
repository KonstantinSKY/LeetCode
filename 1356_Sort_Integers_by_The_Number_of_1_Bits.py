"""1356. Sort Integers by The Number of 1 Bits https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/ """

import time
from typing import List


class Solution:
    def sortByBits1(self, arr: List[int]) -> List[int]:
        return [i[1] for i in sorted([(bin(num).count("1"), num) for num in arr])]

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda n: (bin(n).count('1'), n))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))

    print("--- %s seconds ---" % (time.time() - start_time))
