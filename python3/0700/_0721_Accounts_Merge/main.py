from typing import List
import collections


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToIdx = dict()
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIdx:
                    uf.union(emailToIdx[email], i)
                emailToIdx[email] = i

        parentToIdx = collections.defaultdict(list)
        for i in range(len(accounts)):
            parentToIdx[uf.find(i)].append(i)

        res = list()
        for idxList in parentToIdx.values():
            curRes = [accounts[idxList[0]][0]]
            st = set()
            for idx in idxList:
                for email in accounts[idx][1:]:
                    st.add(email)
            res.append(curRes + sorted(list(st)))
        return res

    def accountsMerge2(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = dict()
        graph = collections.defaultdict(list)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name

            for u, v in zip(account[1:-1], account[2:]):
                graph[u].append(v)
                graph[v].append(u)

        def bfs(x):
            emails = list()
            q = [x]
            while q:
                x = q.pop(0)
                if x not in visited:
                    visited.add(x)
                    emails.append(x)
                    for y in graph[x]:
                        q.append(y)
            return sorted(emails)

        res, visited = list(), set()
        for email in emailToName.keys():
            if email not in visited:
                res.append([emailToName[email]] + bfs(email))
        return res
