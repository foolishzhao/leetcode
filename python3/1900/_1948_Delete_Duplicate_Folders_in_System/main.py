from typing import List
import collections


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = dict()
        dt = collections.defaultdict(list)

        # build tree
        for path in paths:
            cur = tree
            for x in path:
                if x not in cur:
                    cur[x] = dict()
                cur = cur[x]

        def dfs(curNode, curKey, parentNode):
            childKey = tuple(dfs(curNode[key], key, curNode) for key in sorted(curNode.keys()))
            if childKey:
                dt[childKey].append((curKey, parentNode))
            return childKey, curKey

        dfs(tree, None, None)

        for values in dt.values():
            if len(values) > 1:
                for key, parent in values:
                    del parent[key]

        def dfs2(node, curRes, res):
            for key in node.keys():
                res.append(curRes + [key])
                dfs2(node[key], curRes + [key], res)
            return res

        return dfs2(tree, [], [])
