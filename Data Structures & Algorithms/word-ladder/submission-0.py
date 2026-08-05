class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        if len(beginWord) != len(endWord):
            return 0
        
        if endWord not in wordList:
            return 0
        
        def buildPatternStore():
            patternToWord = defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    key = word[:i] + "*" + word[i+1:]
                    patternToWord[key].append(word)
            return patternToWord
        
        patternToWord = buildPatternStore()
        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                for nxt in patternToWord[key]:
                    if nxt not in visited:
                        queue.append((nxt, distance + 1))
                        visited.add(nxt)
                patternToWord[key] = []
        return 0


        