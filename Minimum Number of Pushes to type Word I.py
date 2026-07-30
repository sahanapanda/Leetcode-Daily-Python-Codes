class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        pushes = 0
        
        # Process letters in groups of 8
        for i in range(n):
            # i // 8 gives the position layer (0-indexed)
            # Adding 1 gives the cost per push for that layer
            pushes += (i // 8) + 1
            
        return pushes
