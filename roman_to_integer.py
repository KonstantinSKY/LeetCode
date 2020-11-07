class Solution:
    def romanToInt(self, s: str) -> int:
        roms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = len(s)-1
        res = roms[s[i]]
        while i > 0:
            if roms[s[i]] > roms[s[i - 1]]:
                res -= roms[s[i-1]]
            else:
                res += roms[s[i-1]]
            i -= 1
        return res


if __name__ == "__main__":
    print(Solution().romanToInt("XVII"))
