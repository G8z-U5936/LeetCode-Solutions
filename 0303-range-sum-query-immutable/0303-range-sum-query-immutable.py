class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums

        n = len(self.prefix_sum)
        
        for i in range(1, n): 
            self.prefix_sum[i] = self.prefix_sum[i-1] + self.prefix_sum[i]

    def sumRange(self, left: int, right: int) -> int:
                
        left_sum = 0

        if left > 0:
            left_sum = self.prefix_sum[left-1]

        right_sum = self.prefix_sum[right]

        return right_sum - left_sum

            




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)