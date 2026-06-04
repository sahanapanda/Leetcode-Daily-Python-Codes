class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :type rtype: int
        """
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            # Numbers with fewer than 3 digits have a waviness of 0
            if num < 100:
                continue
                
            s = str(num)
            n = len(s)
            
            # Check every middle digit (from index 1 to n-2)
            for i in range(1, n - 1):
                # Peak condition: strictly greater than both neighbors
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    total_waviness += 1
                # Valley condition: strictly less than both neighbors
                elif s[i] < s[i-1] and s[i] < s[i+1]:
                    total_waviness += 1
                    
        return total_waviness
