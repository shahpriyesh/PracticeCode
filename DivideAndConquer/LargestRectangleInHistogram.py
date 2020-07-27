class Solution:
    def largestRectangleInHistogram_DandC(self, heights):
        if not heights:
            return 0

        min_idx = 0
        min_val = float('inf')
        for i, x in enumerate(heights):
            if x < min_val:
                min_val = x
                min_idx = i

        # Case1: Rectangle constructed by min val and width of arr
        rectangle1 = min_val * len(heights)

        # Case2: Rectangle constructed by elements on left side of min val
        rectangle2 = self.largestRectangleInHistogram_DandC(heights[:min_idx])

        # Case2: Rectangle constructed by elements on right side of min val
        rectangle3 = self.largestRectangleInHistogram_DandC(heights[min_idx+1:])

        return max(rectangle1, rectangle2, rectangle3)


object = Solution()
heights = [6, 4, 5, 2, 4, 3, 9]
print(object.largestRectangleInHistogram_DandC(heights))