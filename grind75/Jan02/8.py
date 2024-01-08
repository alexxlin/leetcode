class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()
        result = 0
        set_sign = False
        for i in range(len(s)):
            if not (s[i] in '-+' or s[i].isnumeric()):
                if sign == 1:
                    return min(result, 2 ** 31 - 1)
                return max(-2 ** 31, -result)
            if s[i] in '-+' or s[i].isnumeric():
                if s[i] in '-+':
                    if set_sign:
                        if sign == 1:
                            return min(result, 2 ** 31 - 1)
                        return max(-2 ** 31, -result)
                    if s[i] == '-':
                        sign = -1
                else:
                    result = result * 10 + int(s[i])
                start = True
            set_sign = True

        if sign == 1:
            return min(result, 2 ** 31 - 1)
        return max(-2 ** 31, -result)
