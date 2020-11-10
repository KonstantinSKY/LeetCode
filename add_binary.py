""" """

import time
from typing import List

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().addBinary('11', '01'))

    print("--- %s seconds ---" % (time.time() - start_time))
