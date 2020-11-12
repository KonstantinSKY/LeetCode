"""1486 XOR Operation in an Array """

import time
from typing import List

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = start
        for i in range(1, n):
            r = r^(start + 2*i)
        return r


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().xorOperation(5, 0))
    print(Solution().xorOperation(4, 3))
    print(Solution().xorOperation(1, 7))

    print("--- %s seconds ---" % (time.time() - start_time))
