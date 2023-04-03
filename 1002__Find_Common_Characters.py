"""1002. Find Common Characters https://leetcode.com/problems/find-common-characters/ """

import time
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        B = [list(i) for i in A]
        while True:
            result = set(B[0]).intersection(*B)
            if not result:
                break
            res.extend(list(result))
            for i in B:
                for j in result:
                    i.remove(j)
        return res





if __name__ == "__main__":
    start_time = time.time()
    print(Solution().commonChars(["label", "bella", "roller"]))
    print(Solution().commonChars(["cool", "lock", "cook"]))

    print("--- %s seconds ---" % (time.time() - start_time))
