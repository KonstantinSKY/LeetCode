"""1652. Defuse the Bomb https://leetcode.com/problems/defuse-the-bomb/ """

import time
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = n * [0]
        code_extended = code * (abs(k) + 1)
        if k > 0:
            for i in range(n):
                res[i] = sum(code_extended[i + 1:i + k + 1])
        elif k < 0:
            k = abs(k)
            for i in range(k * n, (k + 1) * n):
                res[i - k * n] = sum(code_extended[i - k:i])
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().decrypt([5, 7, 1, 4], 3))

    print("--- %s seconds ---" % (time.time() - start_time))
