class Solution:
    def romanToInt(self, s: str) -> int:
        roms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        letters = list(reversed(s))
        res = roms[letters[0]]
        for i in range(1, len(letters)):
            if roms[letters[i]] < roms[letters[i - 1]]:
                res -= roms[letters[i]]
            else:
                res += roms[letters[i]]
        return res


if __name__ == "__main__":
    print(Solution().romanToInt("XVII"))
