from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dt = {"type": 0, "color": 1, "name": 2}
        return sum([item[dt[ruleKey]] == ruleValue for item in items])
