"""1323 https://leetcode.com/problems/maximum-69-number/"""

import time
from typing import List

class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().maximum69Number(9669))
    print(Solution().maximum69Number(9999))
    print("--- %s seconds ---" % (time.time() - start_time))
