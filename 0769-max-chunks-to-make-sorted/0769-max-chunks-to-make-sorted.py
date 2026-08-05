# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         self.chk = arr
#         n = len(arr)
#         mx = 0
#         chunk = 1
#         for i in range(0,n-1):
#             mx = max(mx, arr[i])
#             if mx == i:
#                 chunk += 1
#         return chunk
    # def maxChunksToSorted(self, arr: List[int]) -> int:
    #     self.chk = arr
    #     n = len(arr)
    #     mx = 0
    #     chunk = 1
    #     for i in range(0,n-1):
    #         mx = max(mx, arr[i])
    #         if mx == i:
    #             chunk += 1
    #     return chunk

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 1 0 2 3 4
        self.chk = arr

        # 5
        n = len(arr)

        # 0
        mx = 0

        # 1
        chunk = 1

        # i -> 0, 1, 2, 3
        for i in range(0,n-1):


            mx = max(mx, arr[i])


            # False
            if mx == i:
                chunk += 1

            # 1, 0
            # 1, 1
            # 2, 2
            # 3, 3
            print(mx, i)
            # 1
            # 2
            # 3
            # 4
            print(chunk)

        return chunk
















        #     if mn > min(arr[i]):
        #       mn == min(arr[i])
        #       chunk += 1
        #  return chunk 





            # if mx < i:
            #    mx == arr[i]
            #    chunk += 1  
            # if arr[i] == i:
            #    chunk += 1
            # return chunk
            # if arr[i] == i:
            # chunk += 1
            #  mx = max(mx, arr[i]) 
            #  if(max < i+1):
            #     chunk += 1
            # return chunk
             







        #  return mx
        #  mn = min(arr)
        #  return mn
        #  for i in range(0,n):
        #      if arr[i] == i:
        #         chunk += 1
        #      if arr[0] == mx and arr[-1] == mn:
        #         chunk +=1
        #  return chunk    
         
 