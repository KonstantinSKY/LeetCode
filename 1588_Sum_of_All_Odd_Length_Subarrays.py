""" https://leetcode.com/problems/sum-of-all-odd-length-subarrays/"""

import time
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_odd = 0
        n = len(arr)
        for i in range(1, n + 1, 2):
            for j in range(n - i + 1):
                sum_odd += sum(arr[j: j + i])
        return sum_odd

    def sumOddLengthSubarrays2(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(Solution().sumOddLengthSubarrays([4]))

    print("--- %s seconds ---" % (time.time() - start_time))
