class Solution {
    public int countIslands(int[][] grid, int k) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        int divisibleIslandCount = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // If the cell contains land (> 0) and has not been visited yet
                if (grid[i][j] > 0 && !visited[i][j]) {
                    int islandSum = dfs(grid, visited, i, j, m, n);
                    // Check if the total value of this island is divisible by k
                    if (islandSum % k == 0) {
                        divisibleIslandCount++;
                    }
                }
            }
        }
        
        return divisibleIslandCount;
    }
    
    private int dfs(int[][] grid, boolean[][] visited, int r, int c, int m, int n) {
        // Boundary and validity checks
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] <= 0 || visited[r][c]) {
            return 0;
        }
        
        // Mark the current cell as visited
        visited[r][c] = true;
        int sum = grid[r][c];
        
        // Traverse all 4 cardinal directions (down, up, right, left)
        sum += dfs(grid, visited, r + 1, c, m, n);
        sum += dfs(grid, visited, r - 1, c, m, n);
        sum += dfs(grid, visited, r, c + 1, m, n);
        sum += dfs(grid, visited, r, c - 1, m, n);
        
        return sum;
    }
}
