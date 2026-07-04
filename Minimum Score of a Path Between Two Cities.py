from collections import deque, defaultdict

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :type rtype: int
        :"""
        # Build the adjacency list: graph[node] = [(neighbor, distance), ...]
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # BFS initialization
        queue = deque([1])
        visited = {1}
        min_score = float('inf')
        
        while queue:
            node = queue.popleft()
            
            # Explore all roads connected to the current city
            for neighbor, weight in graph[node]:
                # Track the absolute minimum road weight seen in this component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
