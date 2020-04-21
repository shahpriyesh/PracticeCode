class NextGreaterElement1:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        res = []
        for i in range(len(nums2)-1, -1, -1):
            elem2 = nums2[i]
            if stack and stack[-1] < elem2:
                stack.pop()
            stack.append(elem2)

            if i < len(nums1):
                elem1 = nums1[i]
                j = len(stack)-1
                while j >= 0:
                    if elem1 < stack[j]:
                        res.insert(0, stack[j])
                        break
                    j -= 1

                if j < 0:
                    res.insert(0, -1)

        return res


object = NextGreaterElement1()
print(object.nextGreaterElement([4,1,2], [1,3,4,2]))