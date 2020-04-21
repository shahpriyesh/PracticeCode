class BinaryTreeTilt:
    def findTilt(self, root):
        if not root:
            return 0
        left = self.findTiltUtil(root.left)
        right = self.findTiltUtil(root.right)
        return abs(right-left)

    def findTiltUtil(self, root):
        if not root:
            return 0
        left = self.findTiltUtil(root.left)
        right = self.findTiltUtil(root.right)
        return abs(right-left) + root.val