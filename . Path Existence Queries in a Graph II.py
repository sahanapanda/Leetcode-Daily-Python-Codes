import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Sort nodes by their value while keeping track of their original index
        # sorted_nodes[i] = (value, original_index)
        sorted_nodes = sorted((val, i) for i, val in enumerate(nums))
        
        # Map original index to its position in the sorted array
        pos = [0] * n
        for i, (val, idx) in enumerate(sorted_nodes):
            pos[idx] = i
            
        # Extract just the values for binary searching
        vals = [val for val, idx in sorted_nodes]
        
        # Determine the maximum power of 2 needed for binary jumping
        LOG = 18  # since n <= 10^5, 2^17 = 131072 > 10^5
        
        # up[i][j] stores the index in `sorted_nodes` after 2^j greediest jumps from sorted_nodes[i]
        up = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            # Find the furthest node we can jump to within maxDiff
            limit = vals[i] + maxDiff
            # bisect_right gives the first index with value > limit, so subtract 1
            idx = bisect.bisect_right(vals, limit) - 1
            up[i][0] = idx

        # Populate the sparse table
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # Find the connected components to check if a path exists at all
        comp = [0] * n
        c_id = 0
        for i in range(n):
            if i > 0 and vals[i] - vals[i - 1] > maxDiff:
                c_id += 1
            comp[i] = c_id

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            p_u = pos[u]
            p_v = pos[v]
            
            # Ensure p_u is the one with the smaller value index
            if p_u > p_v:
                p_u, p_v = p_v, p_u
                
            # If they are not in the same connected component, no path exists
            if comp[p_u] != comp[p_v]:
                ans.append(-1)
                continue
            
            # If they are already within maxDiff, it takes exactly 1 step
            if vals[p_v] - vals[p_u] <= maxDiff:
                ans.append(1)
                continue
                
            # Count the steps using binary lifting
            steps = 0
            curr = p_u
            for j in range(LOG - 1, -1, -1):
                # If jumping 2^j steps keeps us strictly below the target index position
                if up[curr][j] < p_v:
                    curr = up[curr][j]
                    steps += (1 << j)
            
            # After the loop, one more jump from `curr` is guaranteed to reach or cross p_v
            # because they are in the same component.
            ans.append(steps + 1)
            
        return ans
