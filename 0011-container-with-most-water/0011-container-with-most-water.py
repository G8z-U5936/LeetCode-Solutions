class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n-1
        mx = 0

        while left < right:
            mx_area = min(height[left],height[right]) * (right - left)
            mx = max(mx, mx_area)

            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx



        