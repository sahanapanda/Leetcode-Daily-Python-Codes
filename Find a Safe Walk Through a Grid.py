from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_cost[r][c] will store the minimum health points lost to reach (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        min_cost[0][0] = grid[0][0]
        
        # Double-ended queue for 0-1 BFS: stores tuples of (row, col)
        dq = deque([(0, 0)])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            r, c = dq.popleft()
            
            # If we reached the bottom-right corner
            if r == m - 1 and c == n - 1:
                break
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    cost = grid[nr][nc]
                    # If we found a path to (nr, nc) with a lower health reduction
                    if min_cost[r][c] + cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = min_cost[r][c] + cost
                        
                        # 0-1 BFS optimization:
                        # If cost is 0, add to front; if cost is 1, add to back.
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
                            
        # We need at least 1 remaining health point, meaning cost incurred must be < health
        return min_cost[m-1][n-1] < health
