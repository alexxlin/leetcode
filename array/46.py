class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #recursion
        
        #nums itself is permutation
        permutations = [nums]
        
        def perm(level, permutations):
            
            #for length of three, there are different levels. at level 1 the first index 
            #will swap with all other indices after it, and pass on to next level.
            #it stops at level 3, all outcomes at level 3 will be returned as all permutations.
            
            if level == len(permutations[0]) - 1:
                return permutations
            
            else:
                new_permutations = []
                for per in permutations:
                    
                    for i in range(level, len(per)):

                        
                        permutation = per.copy()

                        #swapping current index level with later indices
                        permutation[level], permutation[i] = per[i], per[level]

                        new_permutations.append(permutation)
                
                print("new_permutations", new_permutations)
                
                return perm(level + 1, new_permutations)
        
        if nums:
            return perm(0, permutations)
    

                
                
                