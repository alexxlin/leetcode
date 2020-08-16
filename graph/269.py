class Solution:            
    
    def alienOrder(self, words: List[str]) -> str:
        
        #graph, each letter is a node, connecting to the next node/letter
        #if there is cycle, invalid
        #return topological ordering using Kahn's algorithm
        
        #time: O(nk + E) n # of words, k # of characters, nk = # of nodes
        
        #mapping for each unique character in 
        al = {ch: [] for word in words for ch in word}
        indegrees = {ch: 0 for word in words for ch in word}
        
        for word1, word2 in zip(words, words[1:]):
            
            #corner case: word1 is a prefix of word2, then word1 should be beneath word2 instead
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            
            #comparing letter to letter, if first letter is different from second, there is an edge
            #between the two
            for ch1, ch2 in zip(word1, word2):
                
                if ch1 != ch2:
                    al[ch1].append(ch2)
                    indegrees[ch2] += 1
                    break
                    
        
        #Kahn's algorithm for topological sort
        
        zero_degrees = [key for key in indegrees if indegrees[key] == 0]
        result = ""
        
        while zero_degrees:
            
            ch = zero_degrees.pop()
            result += ch
            
            if ch in al:
                for out in al[ch]:

                    indegrees[out] -= 1
                    if indegrees[out] == 0:
                        zero_degrees.append(out)
        
        if len(result) < len(indegrees):
            return ""
        
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        