class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
        def solve(num_str):
            n = len(num_str)
            # memo dictionary to store (idx, tight, is_started, last1, last2)
            # Each entry returns a tuple: (count_of_valid_numbers, sum_of_waviness)
            memo = {}
            
            def dp(idx, tight, is_started, last1, last2):
                if idx == n:
                    # Reached the end of the number, returns (1 valid number, 0 additional waviness)
                    return 1, 0
                
                state = (idx, tight, is_started, last1, last2)
                if state in memo:
                    return memo[state]
                
                limit = int(num_str[idx]) if tight else 9
                total_count = 0
                total_waviness = 0
                
                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    
                    if not is_started:
                        if d == 0:
                            # Leading zero, has not started yet
                            cnt, wav = dp(idx + 1, next_tight, False, -1, -1)
                            total_count += cnt
                            total_waviness += wav
                        else:
                            # First non-zero digit placed
                            cnt, wav = dp(idx + 1, next_tight, True, d, -1)
                            total_count += cnt
                            total_waviness += wav
                    else:
                        # We have already started forming the number
                        # Check if last1 forms a peak or valley with last2 and the current digit d
                        delta = 0
                        if last2 != -1 and last1 != -1:
                            if last1 > last2 and last1 > d:  # Peak
                                delta = 1
                            elif last1 < last2 and last1 < d:  # Valley
                                delta = 1
                        
                        cnt, wav = dp(idx + 1, next_tight, True, d, last1)
                        total_count += cnt
                        # Total waviness contributed by this branch = 
                        # waviness from future steps + (delta * total valid suffix combinations)
                        total_waviness += wav + delta * cnt
                
                memo[state] = (total_count, total_waviness)
                return memo[state]
            
            return dp(0, True, False, -1, -1)[1]

        return solve(str(num2)) - solve(str(num1 - 1))
        
