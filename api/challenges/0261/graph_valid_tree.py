#You have a graph of n nodes labeled from 0 to n - 1. You are given 
# an integer n and a list of edges where edges[i] = [ai, bi] indicates 
# that there is an undirected edge between nodes ai and bi in the graph.

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        if n == 1: return True

        
        adjacency_matrix = [[] for _ in range(n)]

        for a,b in edges:
            adjacency_matrix[a].append(b)
            adjacency_matrix[b].append(a)
        self.ans = True
        seen = set()

        # use DFS to check for cycles. The key points are:
        # If we see a node that's already visited (except the parent), we have a cycle
        # We keep track of visited nodes in a seen set
        # We pass the parent node to avoid counting the edge we came from as a cycle
        def dfs(cur, parent):
            if self.ans == False:
                return 
            for nxt in adjacency_matrix[cur]:
                if nxt in seen and nxt != parent:
                    self.ans = False
                    return  
                if nxt not in seen:
                    seen.add(nxt)
                    dfs(nxt, cur)
        # Finally, I check if:
        # The graph is connected (all nodes were visited)
        # No cycles were found during DFS
        seen.add(edges[0][0])
        dfs(edges[0][0], None)
        return self.ans if len(seen) == len(adjacency_matrix) else False