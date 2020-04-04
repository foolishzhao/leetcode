from typing import List
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dt = collections.defaultdict(list)
        for fr, to in sorted(tickets):
            dt[fr].append(to)

        res = list(['JFK'])
        self.dfs(res, dt, 'JFK', len(tickets) + 1)
        return res

    def dfs(self, res, dt, cur, n):
        if cur not in dt:
            return

        nxts, i = dt[cur], 0
        while i < len(nxts):
            dt[cur] = nxts[:i] + nxts[i + 1:]
            res.append(nxts[i])
            self.dfs(res, dt, nxts[i], n)
            if len(res) == n:
                return
            res.pop()
            i += 1
        dt[cur] = nxts

    # Euler Path
    # Hierholzer’s Algorithm
    # case 1: 一条线可以走过所有的边, 如入栈出栈般获得逆序的路径(排序dt[fr]保证lexical order)
    # case 2: 一条线画完之后还剩别的边, 剩下的边一定组成环, 这条线的尾节点是欧拉path的尾节点, 出栈尾节点, backtrack处理其他节点
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        dt = collections.defaultdict(list)
        for fr, to in sorted(tickets)[::-1]:
            dt[fr].append(to)

        res = list()

        def dfs(cur):
            while dt[cur]:
                dfs(dt[cur].pop())
            res.append(cur)

        dfs('JFK')
        return res[::-1]
