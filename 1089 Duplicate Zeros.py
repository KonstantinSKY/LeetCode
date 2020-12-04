"""1089. Duplicate Zeros https://leetcode.com/problems/duplicate-zeros/ """

import time
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop(-1)
                i += 1
                arr.insert(i, 0)
                print("+")
            i += 1




if __name__ == "__main__":
    start_time = time.time()
    print(Solution().duplicateZeros([1,0,2,3,0,4,5,0]))

    print("--- %s seconds ---" % (time.time() - start_time))
