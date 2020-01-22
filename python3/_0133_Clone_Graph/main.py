class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


from queue import Queue


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        dt = dict()
        dt[node] = Node(node.val, [])

        q = Queue()
        q.put(node)

        while not q.empty():
            cur = q.get()
            for neighbor in cur.neighbors:
                if neighbor not in dt:
                    dt[neighbor] = Node(neighbor.val, [])
                    q.put(neighbor)
                dt[cur].neighbors.append(dt[neighbor])

        return dt[node]
