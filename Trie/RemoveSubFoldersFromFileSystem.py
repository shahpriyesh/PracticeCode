from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.dict = defaultdict(TrieNode)

class RemoveSubFoldersFromFileSystem:
    def removeSubfoldersFromFileSystem(self, folder):
        folder.sort()
        res = []
        root = TrieNode()
        for path in folder:
            path = path.split('/')
            if self.insertInTrie(path, root):
                path = '/'.join(path)
                res.append(path)
        return res

    def insertInTrie(self, path, root):
        curr = root
        for directory in path:
            if directory:
                if curr.isEnd:
                    return False

                curr = curr.dict[directory]
        curr.isEnd = True
        return True


object = RemoveSubFoldersFromFileSystem()
print(object.removeSubfoldersFromFileSystem(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(object.removeSubfoldersFromFileSystem(["/a","/a/b/c","/a/b/d"]))
print(object.removeSubfoldersFromFileSystem(["/a/b/c","/a/b/ca","/a/b/d"]))

# following failed because second entry is subdirectory of first one and not vice versa
print(object.removeSubfoldersFromFileSystem(["/ah/al/am","/ah/al"]))