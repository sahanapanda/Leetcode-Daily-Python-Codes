class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Step 1: Sort the array to process elements greedily
        arr.sort()
        
        # Step 2: The first element must be 1
        arr[0] = 1
        
        # Step 3: Enforce the adjacent difference constraint
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
            
        # The maximum possible element will be at the end of the processed array
        return arr[-1]
