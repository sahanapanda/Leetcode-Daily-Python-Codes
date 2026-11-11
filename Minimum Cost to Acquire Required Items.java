class Solution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long c1 = cost1;
        long c2 = cost2;
        long cBoth = costBoth;
        
        // 1. Cover the overlapping requirement for both types
        long common = Math.min(need1, need2);
        long totalCost = common * Math.min(cBoth, c1 + c2);
        
        // 2. Cover any remaining requirement for type 1
        long rem1 = need1 - common;
        totalCost += rem1 * Math.min(c1, cBoth);
        
        // 3. Cover any remaining requirement for type 2
        long rem2 = need2 - common;
        totalCost += rem2 * Math.min(c2, cBoth);
        
        return totalCost;
    }
}
