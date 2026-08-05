class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegrees = {c:0 for word in words for c in word}
        n = len(words)

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            iterateLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for j in range(iterateLen):
                    if word1[j] != word2[j]:
                        graph[word1[j]].append(word2[j])
                        indegrees[word2[j]] += 1   
                        break  

        queue = deque([])
        for letter, indegree in indegrees.items():
            if indegree == 0:
                queue.append(letter)

        ordering = ""

        while queue:
            char = queue.popleft()
            ordering += char

            for neighbor in graph[char]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(ordering) == len(indegrees):
            return ordering
        else:
            return ""    