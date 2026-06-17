class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
            
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                quotient += 1 << i
                dividend -= divisor << i
                
        return -quotient if negative else quotient