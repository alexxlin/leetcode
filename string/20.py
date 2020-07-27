class Solution:
    def isValid(self, s: str) -> bool:
        
#         if s == "":
#             return True
        
#         mapping = {')': '(', '}': '{', ']': '[' }
        
#         l = []
        
#         for c in s:
            
#             if c not in mapping:
#                 l.append(c)
                
#             else:
#                 if l == [] or l[-1] != mapping[c]:
#                     return False
                
#                 l.pop(-1)
#         return l == []
    
    
        if s=="":
            return True
        dic={'(':0,')':0,'[':0,']':0,'{':0,'}':0}
        for i in range(len(s)):
            dic[s[i]]+=1
        if dic['(']!=dic[')'] or dic['[']!=dic[']'] or dic['{']!=dic['}']:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')' and stack[len(stack)-1]=='(':
                stack.pop()
            elif s[i]==']' and stack[len(stack)-1]=='[':
                stack.pop()
            elif s[i]=='}' and stack[len(stack)-1]=='{':
                stack.pop()
        if stack==[]:
            return True
        return False