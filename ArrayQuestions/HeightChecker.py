class HeightChecker:
    def __init__(self):
        pass

    # performs the task in O(nlgn) time with O(n) space
    # Generic solution that works for any input
    def HeightCheckerUsingSorted(self, heights):
        sorted_heights = sorted(heights)
        counter = 0
        for x, y in zip(sorted_heights, heights):
            if x != y:
                counter += 1
        return counter

    # performs the task in O(n) time with O(100) space
    # works only if given that, heights will be in range on 1 to 100
    def HeightCheckerUsingMap(self, heights):
        height_map = {}
        counter = 0

        # initialize map
        for i in range(101):
            height_map[i] = 0

        # count occurence of heights and store in map
        for height in heights:
            height_map[height] += 1

        current_height = 0
        for height in heights:
            # Reach to first available height in map
            while height_map[current_height] == 0:
                current_height += 1

            # Check if first available height in map is equal to height in heights array
            if current_height != height:
                counter += 1

            # Reduce an occurence of height (doesn't matter whether it was at correct place or not)
            height_map[current_height] -= 1

        return counter