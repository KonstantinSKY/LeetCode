"""1380 Lucky Numbers in a Matrix https://leetcode.com/problems/lucky-numbers-in-a-matrix/ """

import time
from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(nums) for nums in matrix} & {max(nums) for nums in zip(*matrix)})



if __name__ == "__main__":
    start_time = time.time()
    print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))

    print("--- %s seconds ---" % (time.time() - start_time))
