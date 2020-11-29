"""1200. Minimum Absolute Difference https://leetcode.com/problems/minimum-absolute-difference/ """

import time
from typing import List


class Solution:
    def minimumAbsDifference2(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        temp_arr = sorted([[abs(arr[i+1]-arr[i]), arr[i], arr[i+1]] for i in range(len(arr)-1)])
        min = temp_arr[0][0]
        res = [[temp_arr[0][1], temp_arr[0][2]]]

        for i in range(1, len(temp_arr)):
            if temp_arr[i][0] > min:
                break
            res.append([temp_arr[i][1], temp_arr[i][2]])
        return res

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        mini = 10 ** 5 + 1
        miniArr = []

        for i in range(0, len(arr) - 1):
            d = arr[i + 1] - arr[i]
            if d < mini:
                mini = d
                miniArr.clear()
                miniArr.append([arr[i], arr[i + 1]])
            elif d == mini:
                miniArr.append([arr[i], arr[i + 1]])

        return miniArr

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().minimumAbsDifference([3,8, -10,23,19, -4, -14,27]))


    print("--- %s seconds ---" % (time.time() - start_time))
