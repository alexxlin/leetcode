from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_r = Counter(ransomNote)
        c_m = Counter(magazine)

        for key in c_r.keys():
            if key not in c_m or c_m[key] < c_r[key]:
                return False
        
        return True
