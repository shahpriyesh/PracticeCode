class FloodFill:
    def floodFill(self, image, sr, sc, newColor):
        visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        self._fill(image, sr, sc, image[sr][sc], newColor, visited)
        return image

    def _fill(self, image, row, col, oldColor, newColor, visited):
        # boundary check
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
            return

        # visited check
        if visited[row][col]:
            return

        # color check
        if image[row][col] != oldColor:
            return

        # update color and mark visited
        image[row][col] = newColor
        visited[row][col] = True

        # go to next pixels
        self._fill(image, row - 1, col, oldColor, newColor, visited)
        self._fill(image, row + 1, col, oldColor, newColor, visited)
        self._fill(image, row, col - 1, oldColor, newColor, visited)
        self._fill(image, row, col + 1, oldColor, newColor, visited)

        return


object = FloodFill()
image = [[1,1,1],[1,1,0],[1,0,1]]
print(object.floodFill(image, 1, 1, 2))

# because color at pixel is same as newColor, we got into infinite loop
# SOL: had to introduce visited
image = [[0,0,0],[0,1,1]]
print(object.floodFill(image, 1, 1, 1))