"""1528 https://leetcode.com/problems/shuffle-string/ """

import time
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr.count(num) for num in set(arr))) == len(set(arr))


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(Solution().uniqueOccurrences([1, 2]))
    print(Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
    print("--- %s seconds ---" % (time.time() - start_time))
