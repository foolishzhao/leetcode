from typing import List
import collections


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        suffixMp, visited = collections.defaultdict(int), set()
        for i, name in enumerate(names):
            if name in visited:
                suffixMp[name] += 1
                while (name + '(' + str(suffixMp[name]) + ')') in visited:
                    suffixMp[name] += 1
                names[i] = name + '(' + str(suffixMp[name]) + ')'
            visited.add(names[i])
        return names
