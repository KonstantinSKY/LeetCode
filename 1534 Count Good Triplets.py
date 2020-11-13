"""1534 https://leetcode.com/problems/count-good-triplets/ """

import time
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
    print(Solution().countGoodTriplets([1,1,2,2,3], 0, 0, 1))
    print("--- %s seconds ---" % (time.time() - start_time))
