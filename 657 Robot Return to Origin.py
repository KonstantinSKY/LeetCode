"""657 https://leetcode.com/problems/robot-return-to-origin/ """

import time
from typing import List


class Solution:
    def judgeCircle2(self, moves: str) -> bool:
        place = [0, 0]
        for step in moves:
            if step == "L":
                place[0] -= 1
            elif step == "R":
                place[0] += 1
            elif step == "D":
                place[1] -= 1
            elif step == "U":
                place[1] += 1
        return place[0] == 0 and place[1] == 0

    def judgeCircle3(self, moves: str) -> bool:
        place = [0, 0]
        steps = {"L": [-1, 0], "R": [1, 0], "U": [0, +1], "D": [0, -1]}
        for step in moves:
            place[0] += steps[step][0]
            place[1] += steps[step][1]
        return place[0] == 0 and place[1] == 0

    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("L")


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().judgeCircle("DU"))
    print(Solution().judgeCircle("LDRRLRUULR"))

    print("--- %s seconds ---" % (time.time() - start_time))
