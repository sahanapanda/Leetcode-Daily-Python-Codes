class Solution {
    public int divide(int dividend, int divisor) {
        // Handle overflow edge case: -2^31 / -1 = 2^31 (out of 32-bit signed int bounds)
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        // Determine the sign of the result
        // True if signs are different, false if they are the same
        boolean isNegative = (dividend < 0) ^ (divisor < 0);

        // Convert both numbers to long to avoid overflow when using Math.abs
        long absDividend = Math.abs((long) dividend);
        long absDivisor = Math.abs((long) divisor);

        int quotient = 0;

        // Perform bitwise exponential subtraction
        while (absDividend >= absDivisor) {
            long tempDivisor = absDivisor;
            long multiple = 1;

            // Shift left until tempDivisor * 2 exceeds the remaining dividend
            while (absDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }

            // Subtract the largest found multiple from the dividend
            absDividend -= tempDivisor;
            // Add the multiple to the final quotient
            quotient += multiple;
        }

        // Apply the determined sign to the result
        return isNegative ? -quotient : quotient;
    }
}
