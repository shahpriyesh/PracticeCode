class SimplifyPath:
    def simplifyPath(self, path):
        path = path.split('/')
        stack = []
        for dir in path:
            if dir:
                if dir == '..':
                    if stack:
                        stack.pop()
                elif dir == '.':
                    continue
                else:
                    stack.append(dir)
        s = '/' + '/'.join(stack)
        return s


object = SimplifyPath()
print(object.simplifyPath("/home/"))
print(object.simplifyPath("/../"))
print(object.simplifyPath("/home//foo/"))
print(object.simplifyPath("/a/./b/../../c/"))
print(object.simplifyPath("/a/../../b/../c//.//"))
print(object.simplifyPath("/a//b////c/d//././/.."))
