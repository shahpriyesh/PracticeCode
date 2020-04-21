from Trie.TrieNode import TrieNode

class SearchSuggestionSystem:
    def searchSuggestionSystem(self, products, searchWord):
        final = []
        root = TrieNode()
        for product in products:
            curr = root
            for c in product:
                idx = ord(c) - ord('a')
                if not curr.charList[idx]:
                    curr.charList[idx] = TrieNode()
                curr = curr.charList[idx]
            curr.isWord = True

        curr = root
        word = ""
        for c in searchWord:
            res = []
            word += c
            idx = ord(c) - ord('a')
            if curr.charList[idx]:
                curr = curr.charList[idx]
                self.searchOptions(curr, word, res)
            final.append(res)

        return final


    def searchOptions(self, root, word, res):
        if not root or len(res) >= 3:
            return

        if root.isWord and len(res) < 3:
            res.append(word)

        for idx, node in enumerate(root.charList):
            c = chr(idx + ord('a'))
            word += c
            self.searchOptions(node, word, res)
            word = word[0:len(word)-1]


    def printTrie(self, root, word):
        if not root:
            return

        if root.isWord:
            print(word)

        for idx, node in enumerate(root.charList):
            c = chr(idx + ord('a'))
            word += c
            self.printTrie(node, word)
            word = word[0:len(word)-1]


object = SearchSuggestionSystem()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
print(object.searchSuggestionSystem(products, "mouse"))
products = ["havana"]
print(object.searchSuggestionSystem(products, "havana"))
products = ["bags", "baggage", "banner", "box", "cloths"]
print(object.searchSuggestionSystem(products, "bags"))
products = ["havana"]
print(object.searchSuggestionSystem(products, "tatiana"))