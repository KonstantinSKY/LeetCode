"""1313. https://leetcode.com/problems/decompress-run-length-encoded-list/"""

import time
from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res.extend(nums[i]*[nums[i+1]])
        return res

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().decompressRLElist([1,2,3,4]))
    print(Solution().decompressRLElist([1,1,2,3]))

    print("--- %s seconds ---" % (time.time() - start_time))
