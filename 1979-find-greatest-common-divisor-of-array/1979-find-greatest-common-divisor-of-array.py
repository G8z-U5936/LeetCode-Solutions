class Solution:
    def findGCD(self, nums: List[int]) -> int:
        self.gcd = nums
        n = len(nums)
        ans = 0
        mn = min(nums)
        mx = max(nums)
        ans = gcd(mn,mx)
        
        return ans
 
    def gcd(self,a: int , b: int) -> int:
        if a==0 and b==0:
           print(undefined)
        if b==0:
           return a
        return self.gcd(b, a % b)
 
       
