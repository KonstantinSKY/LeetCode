"""412. Fizz Buzz https://leetcode.com/problems/fizz-buzz/"""

import time
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            r = ""
            if i % 3 == 0:
                r += "Fizz"
            if i % 5 == 0:
                r += "Bizz"
            if not r:
                r = str(i)
            res.append(r)
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().fizzBuzz(15))

    print("--- %s seconds ---" % (time.time() - start_time))
