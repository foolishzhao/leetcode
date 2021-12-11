import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str2 = collections.defaultdict(list)
        for i in range(len(strs)):
            str2[''.join(sorted(strs[i]))].append(strs[i])

        return str2.keys()
if __name__ == '__main__':
    arr = ["eat","tea","tan","ate","nat","bat"]
    ans = Solution().groupAnagrams(arr)
    print("----answser-----")
    print(ans)



