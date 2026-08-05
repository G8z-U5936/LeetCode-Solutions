class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB)//2
        bobset = set(bobSizes)

        for x in aliceSizes:
            y = x - diff
            if y in bobset:
                return [x,y]
    
# without set:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB)//2
        
        for x in aliceSizes:
            for y in bobSizes:
                if x - y == diff:
                    return [x,y]

