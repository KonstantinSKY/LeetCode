"""1. https://leetcode.com/problems/two-sum/"""

from typing import List


class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i, num in enumerate(nums):
            delta = target - num
            if delta not in index_dict:
                index_dict.update({num: i})
            else:
                return [index_dict[delta], i]


if __name__ == "__main__":
    print(Solution().two_sum([3, 2, 4], 6))
