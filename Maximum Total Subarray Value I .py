class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Find the global maximum difference in the array
        max_val = max(nums)
        min_val = min(nums)
        
        # Multiply the maximum single subarray value by k
        return (max_val - min_val) * k
        
