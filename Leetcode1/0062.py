class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m == 1 or n == 1:
            return 1
        
        dp = [ [1] * n ] * m
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
