from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_len = 0
        
        # 1. Handle the special case for number 1
        if 1 in counts:
            # We must choose an odd number of 1s
            max_len = counts[1] if counts[1] % 2 != 0 else counts[1] - 1
            
        # 2. Iterate through all other possible starting elements > 1
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            # Keep climbing the squares while we have at least 2 copies of the current number
            while counts[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            # If the peak element exists at least once, it completes the center of the pattern
            if counts[curr] >= 1:
                current_len += 1
            else:
                # If it doesn't exist, the previous element must become the peak instead of a wing
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len
