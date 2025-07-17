class Solution:
    def maxCoins(self, nums):
        # Add 1 at the beginning and end to handle boundaries
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Memoization table
        dp = [[0] * n for _ in range(n)]

        # Interval length starts from 2 (i.e., min distance between left and right)
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    )
        
        return dp[0][n - 1]
