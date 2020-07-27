class Solution:
    def stringCompression(self, chars):
        res = []
        curr = chars[0]
        count = 1

        for c in chars[1:]:
            if c == curr:
                count += 1
            else:
                res.append(curr)
                if count > 1:
                    res.extend(self.appendCount(count))

                curr = c
                count = 1

        res.append(curr)
        if count > 1:
            res.extend(self.appendCount(count))

        chars = res
        return len(res)

    def appendCount(self, count):
        temp = []
        while count > 0:
            temp.append(str(count % 10))
            count = count // 10
        return temp[::-1]


object = Solution()
print(object.stringCompression(["a","a","b","b","c","c","c"]))
print(object.stringCompression(["a"]))
print(object.stringCompression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))