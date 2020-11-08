import time

class Solution:
    def romanToInt(self, s: str) -> int:
        roms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = len(s)-1
        res = curr = roms[s[i]]
        while i > 0:
            prev = roms[s[i - 1]]
            if curr > prev:
                res -= prev
            else:
                res += prev
            i -= 1
            curr = prev
        return res

    def intToRoman(self, num: int) -> str:
        roms = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",  40: "XL", 50: "L",
                90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        res = ""
        for i in sorted(roms.keys(), reverse=True):
            res += roms[i] * (num // i)
            num %= i
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().romanToInt("MCMXCIV"))
    #print(Solution().intToRoman(400))
    print("--- %s seconds ---" % (time.time() - start_time))
