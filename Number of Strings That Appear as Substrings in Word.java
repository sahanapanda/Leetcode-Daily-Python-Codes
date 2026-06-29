class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        # Count how many patterns are a substring of word
        return sum(1 for pattern in patterns if pattern in word)
