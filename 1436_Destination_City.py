"""1436 https://leetcode.com/problems/destination-city/"""

import time
from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a, b = zip(*paths)
        for i in range(len(a)):
            if b[i] not in a:
                return b[i]



    def destCity2(self, paths: List[List[str]]) -> str:
        paths_d = {path[0]: path[1] for path in paths}
        for path in paths:
            if path[1] not in paths_d:
                return path[1]

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().destCity([["B","C"],["D","B"],["C","A"]]))

    print("--- %s seconds ---" % (time.time() - start_time))
