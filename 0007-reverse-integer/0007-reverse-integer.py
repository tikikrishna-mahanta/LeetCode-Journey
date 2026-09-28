class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            res = res * 10 + digit
            
        res *= sign
        
        if res < INT_MIN or res > INT_MAX:
            return 0
            
        return res
