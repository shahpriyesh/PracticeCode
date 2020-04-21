class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class AverageOfLevels:
    def __init__(self):
        pass

    def averageOfLevels(self, root: TreeNode):
        response = []
        queue = []

        total = 0
        count = 0
        prev_level = 1

        if root is None:
            return response

        temp = (root, 1)
        queue.append(temp)

        while queue:
            temp = queue.pop(0)
            current = temp[0]
            level = temp[1]

            if level == prev_level:
                total += current.val
                count += 1
            else:
                response.append(total / count)
                total, count = 0, 0
                total += current.val
                count += 1
                prev_level = prev_level + 1

            if current.left is not None:
                queue.append((current.left, level + 1))
            if current.right is not None:
                queue.append((current.right, level + 1))

        response.append(total / count)

        return response


node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

object = AverageOfLevels()
print(object.averageOfLevels(node))