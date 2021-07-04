from typing import List
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = collections.defaultdict(int)

        i, prev = 0, None
        for j, c in enumerate(paragraph + ' '):
            if not c.isalpha():
                if prev and prev.isalpha():
                    counter[paragraph[i: j].lower()] += 1
                i = j + 1
            prev = c

        maxW, maxC = None, 0
        for w, c in counter.items():
            if w not in banned and c > maxC:
                maxC = c
                maxW = w
        return maxW


if __name__ == '__main__':
    Solution().mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        ["hit"],
    )
