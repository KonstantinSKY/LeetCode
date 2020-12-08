"""509. Fibonacci Number  https://leetcode.com/problems/fibonacci-number/ """

import time
from typing import List

class Solution:
    def fib(self, N: int) -> int:
        fib_arr = [0, 1]
        for i in range(2, N+1):
            fib_arr.append(fib_arr[0] + fib_arr[1])
        return fib_arr[N]

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().fib(3))
    print(Solution().fib(10))
    print(Solution().fib(0))
    print(Solution().fib(1))
    print("--- %s seconds ---" % (time.time() - start_time))
