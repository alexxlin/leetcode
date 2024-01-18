from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = Counter(p)
        n = len(p)
        current = defaultdict(int)
        result = []
        for i in range(n-1):
            current[s[i]] += 1
        i = 0
        while i <= len(s) - n:
            current[s[i+n-1]] += 1
            if current == target:
                result.append(i)
            current[s[i]] -= 1
            if current[s[i]] == 0:
                del current[s[i]]
            i += 1
        return result
