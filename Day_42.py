class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Extract non-zero digits as a string
        digits = [c for c in str(n) if c != '0']
        
        # If there are no non-zero digits, x is 0
        if not digits:
            return 0
        
        # Form the new integer x
        x = int("".join(digits))
        
        # Calculate the sum of digits in x
        digit_sum = sum(int(c) for c in digits)
        
        # Return the product
        return x * digit_sum
