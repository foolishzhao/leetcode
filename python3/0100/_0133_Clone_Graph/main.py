class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def bfs(cur):
            q = [cur]
            while q:
                cur = q.pop(0)
                for x in cur.neighbors:
                    if x not in dt:
                        dt[x] = Node(x.val)
                        q.append(x)
                    dt[cur].neighbors.append(dt[x])

        def dfs(cur):
            for x in cur.neighbors:
                if x not in dt:
                    dt[x] = Node(x.val)
                    dfs(x)
                dt[cur].neighbors.append(dt[x])

        dt = dict()
        dt[node] = Node(node.val)
        dfs(node)
        return dt[node]
