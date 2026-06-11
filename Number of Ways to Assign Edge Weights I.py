rom collections import defaultdict

class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Find the maximum depth using DFS
        max_depth = 0
        
        # Stack stores tuples of (current_node, parent_node, current_depth)
        stack = [(1, -1, 0)]
        
        while stack:
            node, parent, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
                
            for neighbor in adj[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, depth + 1))
        
        # Step 3: Compute 2^(max_depth - 1) % (10^9 + 7)
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
