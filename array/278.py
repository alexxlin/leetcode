# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #time: O(logn)
        #space: O(1)
        
        def recursive_check(left, right):
            
            
            #we have pinpointed the first bad version
            if left == right:
                return left
            
            #the interval contains two versions only
            elif left == right - 1:
                if isBadVersion(left):
                    return left
                return right
            
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            
            else:
                left = mid
            
            return recursive_check(left, right)
        

        return recursive_check(1, n)