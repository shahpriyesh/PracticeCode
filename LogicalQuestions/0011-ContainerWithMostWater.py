class ContainerWithMostWater:
    def __init__(self):
        pass

    def containerWithMostWater(self, height):
        arr_len = len(height)
        if arr_len < 2:
            return 0

        max_water = 0

        left, right = 0, arr_len-1
        while left < right:
            h = height[left] if height[left] < height[right] else height[right]
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_water


object = ContainerWithMostWater()
height = [1,8,6,2,5,4,8,3,7]
print(object.containerWithMostWater(height))