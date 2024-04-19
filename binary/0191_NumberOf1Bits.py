class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1  # Check if the rightmost bit is 1
            n >>= 1         # Right-shift to check the next bit
        return count
    

### Second method 
"""
class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1  # Check if the rightmost bit is 1
            n >>= 1         # Right-shift to check the next bit
        return count
"""