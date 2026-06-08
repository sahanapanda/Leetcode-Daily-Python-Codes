class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :type rtype: List[int]
        """
        less = []
        equal = []
        greater = []
        
        # Partition elements into three separate lists
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        # Combine the lists to get the final partitioned array
        return less + equal + greater
