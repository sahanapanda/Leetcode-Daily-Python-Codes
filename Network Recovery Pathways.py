from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        
        # Pre-build adjacency list with all edges for efficient filtering
        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
                
        # Compute in-degrees for topological sort
        in_degree_orig = [0] * n
        for u in range(n):
            for v, cost in graph[u]:
                in_degree_orig[v] += 1

        def check(min_allowed_edge):
            # DP array to track the minimum path cost to reach each node
            dist = [float('inf')] * n
            dist[0] = 0
            
            # Use Kahn's algorithm for topological sort, filtering by edge cost
            in_degree = list(in_degree_orig)
            queue = deque([i for i in range(n) if in_degree[i] == 0])
            
            while queue:
                u = queue.popleft()
                
                for v, cost in graph[u]:
                    # Only consider edges that satisfy the binary search condition
                    if cost >= min_allowed_edge:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                    
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            return dist[n - 1] <= k

        # Binary search range based on edge costs
        low = 0
        high = max([edge[2] for edge in edges]) if edges else 0
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2  # Fixed the formula and removed the typo line
            
            if check(mid):
                ans = mid      # mid is possible, try to find a larger minimum edge
                low = mid + 1
            else:
                high = mid - 1 # mid is too large, lower the threshold
                
        return ans
