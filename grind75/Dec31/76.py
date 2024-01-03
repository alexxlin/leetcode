from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        # frequency of the character in t appearing in the sliding 
window
        d = defaultdict(int)
        # result's length
        result_length = math.inf
        # left and right indices of the result_length
        result_left = -1
        result_right = -1
        # required characters and freq of t
        counter = Counter(t)
        left, right = 0, 0
        # number of characters with enough frequencies
        formed = 0
        # total number of distinct characters in t
        required_formed = len(counter)
        while right < len(s):
            character = s[right]
            if character not in counter:
                right += 1
                continue
            d[character] += 1
            if d[character] == counter[character]:
                formed += 1
            
            if formed == required_formed:
                while left <= right:
                    left_character = s[left]
                    if left_character in counter:
                        if d[left_character] > counter[left_character]:
                            d[left_character] -= 1
                        else:
                            break

                    left += 1
                
                if result_length > (right - left + 1):
                    result_length = right - left + 1
                    result_left = left
                    result_right = right
            right += 1

        if formed != required_formed:
            return ""
        return s[result_left:result_right + 1]

