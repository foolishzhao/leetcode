class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # confirm if version can be like "xx..xx"
        v1 = [int(x) if x else 0 for x in version1.split(".")]
        v2 = [int(x) if x else 0 for x in version2.split(".")]

        n1, n2, i = len(v1), len(v2), 0
        while i < n1 and i < n2:
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1

        while i < n1:
            if v1[i] > 0:
                return 1
            i += 1

        while i < n2:
            if v2[i] > 0:
                return -1
            i += 1

        return 0
