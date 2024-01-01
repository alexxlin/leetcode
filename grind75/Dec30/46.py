class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        m = len(nums)
        def dfs(perm, current_i):
            if current_i == m - 1:
                result.append(perm)
                return
            for i in range(current_i, m):
                new_perm = perm.copy()
                new_perm[i], new_perm[current_i] = new_perm[current_i], 
new_perm[i]
                dfs(new_perm, current_i + 1)
        dfs(nums, 0)
        return result
