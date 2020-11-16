""" https://leetcode.com/problems/sum-of-all-odd-length-subarrays/"""

import time
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        new_arr = []
        for i in range(1, len(arr) + 1, 2):
            new_arr.extend([sum(arr[j: j + i]) for j in range(len(arr) - i + 1)])
        return sum(new_arr)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(Solution().sumOddLengthSubarrays([4]))

    print("--- %s seconds ---" % (time.time() - start_time))
