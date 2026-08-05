class Solution:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.word = ""
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = self.TrieNode()
        for word in words:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = self.TrieNode()
                curr = curr.children[ch]
            curr.word = word
        
        res = []
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m , n = len(board), len(board[0])

        def dfs(r , c , curNode):
            ch = board[r][c]

            if ch not in curNode.children:
                return
            
            nxt = curNode.children[ch]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            
            board[r][c] = "#"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<m and 0<=nc<n and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            
            board[r][c] = ch
        
        for i in range(m):
            for j in range(n):
                dfs(i , j, self.root)
    
        return res
            

        