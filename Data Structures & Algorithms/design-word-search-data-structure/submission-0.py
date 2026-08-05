class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        def dfs(index, curNode):
            if index == len(word):
                return curNode.endOfWord
            
            if word[index] == ".":
                for letter in curNode.children.values():
                    if dfs(index + 1, letter):
                        return True
                    
                return False
            else:
                if word[index] not in curNode.children:
                    return False
                return dfs(index + 1, curNode.children[word[index]])
        
        return dfs(0, self.root)
        
