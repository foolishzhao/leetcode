"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections

from python3.common.define import Node


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {node: Node(node.val)}
        st = [node]
        while st:
            n = st.pop(0)
            for neigh in n.neighbors:
                if neigh not in m:
                    st.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]

    def cloneGraph(self, node):  # DFS recursively
        if not node:
            return node
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])



