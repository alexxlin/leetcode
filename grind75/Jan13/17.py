class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.n = len(digits)
        self.mapping = 
{'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.result = []
        self.digits = digits
        self.recursive('', 0)

        return self.result

    def recursive(self, prefix, index):
        if index == self.n:
            self.result.append(prefix)
            return

        for char in self.mapping[self.digits[index]]:
            self.recursive(prefix+char, index+1)
