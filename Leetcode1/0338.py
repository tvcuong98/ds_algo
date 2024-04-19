class Solution(object):
    def countBits(self, n):
        result = [0] * (n + 1)  # Store the counts
        for i in range(1, n + 1):
            result[i] = result[i // 2] + (i % 2)  # Apply the pattern
        return result