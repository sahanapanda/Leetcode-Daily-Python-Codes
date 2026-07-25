class Solution {
    public int maxProduct(int n) {
        int max1 = -1;
        int max2 = -1;
        
        // Extract each digit from the number
        while (n > 0) {
            int digit = n % 10;
            n /= 10;
            
            // Update the two largest digits
            if (digit >= max1) {
                max2 = max1;
                max1 = digit;
            } else if (digit > max2) {
                max2 = digit;
            }
        }
        
        return max1 * max2;
    }
}
