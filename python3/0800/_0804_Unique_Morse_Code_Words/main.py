from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        st = set()
        for w in words:
            morse = ""
            for c in w:
                morse += tab[ord(c) - ord('a')]
            st.add(morse)
        return len(st)
