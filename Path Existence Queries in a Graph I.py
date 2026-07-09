class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Array to store the component ID for each node
        comp = [0] * n
        curr_id = 0
        
        # Determine continuous connected components
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curr_id += 1
            comp[i] = curr_id
            
        # Answer each query in O(1) time
        return [comp[u] == comp[v] for u, v in queries]
