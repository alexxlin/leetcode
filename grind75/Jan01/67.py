class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        
        if not b:
            return a
        
        if int(a[-1]) + int(b[-1]) == 2:
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + 
'0'
        
        return self.addBinary(a[:-1], b[:-1]) + str(int(a[-1]) + 
int(b[-1]))
