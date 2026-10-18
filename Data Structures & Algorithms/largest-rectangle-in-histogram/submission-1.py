class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        tmp = []

        max_area = 0

        for i in range(len(heights)+1):
            curr_height = heights[i] if i<len(heights) else 0
            while tmp and  curr_height < heights[tmp[-1]]:

                last = tmp.pop()
                next_small = i
                prev_small = tmp[-1] if tmp else -1
                width =  next_small - prev_small - 1
                area = heights[last] * width
                max_area = max(max_area, area)

            tmp.append(i)

        return max_area