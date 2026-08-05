from typing import  List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score_with_index = [(s,i) for i,s in enumerate(score)]
        score_with_index.sort(key= lambda x:x[0],reverse = True)
        result  = [""] * n
        for rank,(s,i) in enumerate(score_with_index):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank+1)
        return result
