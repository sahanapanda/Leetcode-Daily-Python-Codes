class Solution:
    def canReach(self, arr, start):
        visited = set()

        def dfs(i):
            # out of bounds or already visited
            if i < 0 or i >= len(arr) or i in visited:
                return False

            # found zero
            if arr[i] == 0:
                return True

            visited.add(i)

            # try both directions
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
        
