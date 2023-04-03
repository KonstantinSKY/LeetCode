"""1491. Average Salary Excluding the Minimum and Maximum Salary https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/ """

import time
from typing import List

class Solution:
    def average1(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / len(salary[1:-1])

    def average(self, salary: List[int]) -> float:
        new = sorted(salary)[1:-1]
        return sum(new) / len(new)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().average([4000,3000,1000,2000]))

    print("--- %s seconds ---" % (time.time() - start_time))
