class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> 
List[List[int]]:
        result = []
        def dfs(prefix, current_sum, current_i):
            if current_sum == target:
                result.append(prefix)
                return
            for i in range(current_i, len(candidates)):
                if current_sum + candidates[i] <= target:
                    dfs(prefix + [candidates[i]], current_sum + 
candidates[i], i)
        
        dfs([], 0, 0)
        return result
