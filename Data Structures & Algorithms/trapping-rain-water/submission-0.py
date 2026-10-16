class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0

        right = len(height) - 1
        left_max = 0
        right_max = 0

        ans = 0

        while left < right:

            if height[left] < height[right]:

                if height[left] < left_max:
                    ans = ans + left_max - height[left]
                else:
                    left_max = height[left]
                left = left + 1

            else:
                if height[right] < right_max:
                    ans = ans + right_max - height[right]
                else:
                    right_max = height[right]
                right = right -1

        return ans