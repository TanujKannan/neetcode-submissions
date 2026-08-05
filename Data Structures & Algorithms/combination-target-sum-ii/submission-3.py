class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        n = len(candidates)

        path = []

        def dfs(start, remaining):
            if remaining == 0:
                res.add(tuple(path[:]))
            
            for i in range(start, n):
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])

                dfs(i + 1, remaining - candidates[i])

                path.pop()
        
        dfs(0 , target)
        return list(list(tup) for tup in res)
                

        