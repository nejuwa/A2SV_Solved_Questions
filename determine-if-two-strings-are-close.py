class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        if set(word1) != set(word2):
            return False
        
        return sorted(count1.values()) == sorted(count2.values())
