class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #time: O(max(a,b)) a carry would travel across all of max(a,b) digits
        #space: O(1) extra memory, O(max(n, m)) for the answer
        
        #1. my version, recursion
        
#         if a and b:
#             if int(a[-1]) + int(b[-1]) <= 1:
#                 return self.addBinary(a[:-1], b[:-1]) + str(int(a[-1]) + int(b[-1]))
#             else:
#                 return self.addBinary(self.addBinary(a[:-1], "1"), b[:-1]) + "0"
            
#         if not a:
#             return b
            
#         if not b:
#             return a
                   
        #2. solution bit manipulation
        
        #bit manipulation can be applied directly on ints
        #XOR makes lots of things easier
        #bin(int) returns "0b" + bit version of int
                
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]        
            
            
            