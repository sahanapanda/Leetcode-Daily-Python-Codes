class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        
        # Initialize DP tables
        # dp_score[i][j] will store the max score to reach (i, j) from 'S'
        # dp_paths[i][j] will store the number of paths to achieve that max score
        dp_score = [[0] * n for _ in range(n)]
        dp_paths = [[0] * n for _ in range(n)]
        
        # Base case: Starting position 'S' at bottom-right
        dp_paths[n-1][n-1] = 1
        
        # Iterate from the bottom-right corner up to the top-left corner
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip the starting point since it's already initialized
                if i == n - 1 and j == n - 1:
                    continue
                # Skip obstacles
                if board[i][j] == 'X':
                    continue
                
                max_score = -1
                total_paths = 0
                
                # Check the 3 possible choices we could have come from:
                # 1. Down (i+1, j), 2. Right (i, j+1), 3. Down-Right (i+1, j+1)
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for r, c in directions:
                    if r < n and c < n and dp_paths[r][c] > 0:
                        if dp_score[r][c] > max_score:
                            max_score = dp_score[r][c]
                            total_paths = dp_paths[r][c]
                        elif dp_score[r][c] == max_score:
                            total_paths = (total_paths + dp_paths[r][c]) % MOD
                
                # If at least one valid incoming path exists
                if max_score != -1:
                    current_val = 0
                    if board[i][j] != 'E':
                        current_val = int(board[i][j])
                    
                    dp_score[i][j] = max_score + current_val
                    dp_paths[i][j] = total_paths
                    
        # The answer for the destination 'E' at (0, 0)
        return [dp_score[0][0], dp_paths[0][0]]
