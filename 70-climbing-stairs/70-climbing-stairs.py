class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return(n)
        if n == 2:
            return(2)
        
        F = {0:0,1:1,2:2}
        
        s_1 = s_2 = 0
        
        for i in range(3,n+1):
            s_1,s_2 = F[i-1],F[i-2]
            F[i] = s_1 + s_2
        return (F[n])