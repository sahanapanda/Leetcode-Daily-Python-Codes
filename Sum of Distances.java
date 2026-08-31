import java.util.*;

class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] arr = new long[n];
        
        // Map to store value -> list of its indices
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        
        // Calculate the absolute differences using prefix sums
        for (List<Integer> indices : map.values()) {
            int k = indices.size();
            if (k <= 1) continue; // No other identical element exists
            
            // Calculate total sum of indices for this group
            long totalSum = 0;
            for (int idx : indices) {
                totalSum += idx;
            }
            
            long leftSum = 0;
            for (int m = 0; m < k; m++) {
                long currentIdx = indices.get(m);
                long rightSum = totalSum - leftSum - currentIdx;
                
                long leftCount = m;
                long rightCount = k - 1 - m;
                
                // Formula implementation
                long leftTotal = (leftCount * currentIdx) - leftSum;
                long rightTotal = rightSum - (rightCount * currentIdx);
                
                arr[(int) currentIdx] = leftTotal + rightTotal;
                
                // Update left running sum for the next element
                leftSum += currentIdx;
            }
        }
        
        return arr;
    }
}
