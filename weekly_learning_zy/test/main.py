import collections
import copy
from typing import List


class Solution:
    def rmduplicated(self, str):
        # a = set(str)
        # return list(a)
        str.sort()
        i = 0
        n = len(str)
        for j in range(1, n):
            if str[j] > str[i]:
                i += 1
                str[i] = str[j]
        return str[:i+1]
    def diagonal(self,tmp):
        height = len(tmp)
        width = len(tmp[0])
        small = []
        dia = []
        bigger = []
        for i in range(width):
            for j in reversed(range(height)):

                if j == width -1:
                    print()
        return bigger + dia+ small




if __name__ == '__main__':

    a = [4,4,1,1,1,2,2,3]
    b = [[1,2,3,5],[5,6,7,8],[9,10,11,12]]
    res = Solution().diagonal(b)
    print(res)
    # b ="aabbccd"
    # ans =[]
    # counter = collections.Counter(a)
    # d = counter.most_common()
    # k = 2
    # for i in range(k):
    #     ans.append(d[i][0])
    # print(ans)
    # print(counter.items())
    # print(d)
