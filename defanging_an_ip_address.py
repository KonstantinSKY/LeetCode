""" https://leetcode.com/problems/defanging-an-ip-address/"""

import time
from typing import List

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().defangIPaddr("255.100.50.0"))
    print(Solution().defangIPaddr("1.1.1.1"))


    print("--- %s seconds ---" % (time.time() - start_time))
