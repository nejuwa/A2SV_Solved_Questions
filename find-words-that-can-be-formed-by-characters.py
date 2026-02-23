class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars) 
        s=0   
        for word in words:
            if not (Counter(word) - count):
                s+=len(word)
        return s

