class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(current_permutation, remaining_nums):
            # Base case: if no numbers are left, we've formed a full permutation
            if not remaining_nums:
                result.append(current_permutation)
                return
            
            for i in range(len(remaining_nums)):
                # Choose an element and recurse with the rest
                backtrack(
                    current_permutation + [remaining_nums[i]], 
                    remaining_nums[:i] + remaining_nums[i+1:]
                )
        
        backtrack([], nums)
        return result
