"""1450 https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/ """

import time
from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            count += 1 if startTime[i] <= queryTime <= endTime[i] else 0
        return count

    def busyStudent2(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
            res = 0
            for start, end in zip(startTime, endTime):
                res += (start <= queryTime <= end)
            return res

    class Solution:
        def busyStudent3(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
            return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().busyStudent([1, 2, 3], [3, 2, 7], 4))

    print("--- %s seconds ---" % (time.time() - start_time))
