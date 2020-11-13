""" 804 https://leetcode.com/problems/unique-morse-code-words/"""

import time
from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        words_morse = []
        for word in words:
            word_morse = ""
            for letter in word:
                word_morse += alphabet[ord(letter)-97]
            words_morse.append(word_morse)
        return len(set(words_morse))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

    print("--- %s seconds ---" % (time.time() - start_time))
