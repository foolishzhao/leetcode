from typing import List
import collections


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.childs = collections.defaultdict(list)
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.childs[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(x):
            curOrder.append(x)
            for y in self.childs[x]:
                dfs(y)

        curOrder = list()
        dfs(self.king)
        return [x for x in curOrder if x not in self.deaths]
