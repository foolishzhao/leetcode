from typing import List
import collections


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dt = collections.defaultdict(int)
        for cpdomain in cpdomains:
            fields = cpdomain.split()
            cnt = int(fields[0])

            ds = fields[1].split('.')
            for i in range(len(ds) - 1, -1, -1):
                dt['.'.join(ds[i:])] += cnt

        return [str(cnt) + ' ' + d for d, cnt in dt.items()]

    def subdomainVisits2(self, cpdomains: List[str]) -> List[str]:
        dt = collections.defaultdict(int)
        for cpdomain in cpdomains:
            fields = cpdomain.split()
            dt[fields[1]] += int(fields[0])
            for i, c in enumerate(fields[1]):
                if c == '.':
                    dt[fields[1][i + 1:]] += int(fields[0])

        return [str(cnt) + ' ' + d for d, cnt in dt.items()]
