class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = {word: i for i, word in enumerate(list1)}
        msum = float('inf')
        result = []
        for j, word in enumerate(list2):
            if word in l1:
                ind = j + l1[word]
                
                if ind < msum:
                    msum = ind
                    result = [word]  
                elif ind == msum:
                    result.append(word)
        
        return result




