class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictlist1 = {}
        dictlist2 = {}
        result = []

        for idx,num in enumerate(list1):
            dictlist1[num] = idx
        
        for idx,num in enumerate(list2):
            if num in dictlist1:
                dictlist2[num] = idx + dictlist1[num]
            
        min_sum = min(dictlist2.values())

        for key,value in dictlist2.items():
            if value == min_sum:
                result.append(key)
            
        return result


        

                
            
        
        