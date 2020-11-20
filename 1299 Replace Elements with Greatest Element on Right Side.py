"""1299 https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/ """

import time
from typing import List


class Solution:
    def replaceElements2(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1:])
        arr[-1] = -1
        return arr

    def replaceElements(self, arr: List[int]) -> List[int]:
        new = [max(arr[i + 1:]) for i in range(len(arr) - 1)]
        new.append(-1)
        return new


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))

    print("--- %s seconds ---" % (time.time() - start_time))
