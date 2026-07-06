class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(n - 1):
            next_str = []
            count = 1
            
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    next_str.append(str(count))
                    next_str.append(result[i - 1])
                    count = 1
            
            next_str.append(str(count))
            next_str.append(result[-1])
            
            result = "".join(next_str)
            
        return result