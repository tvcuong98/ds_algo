class Solution(object):
    def getSum(self, a, b):
        # 32-bit mask in hexadecimal to handle negative cases 
        MASK = 0xFFFFFFFF 

        # Works both as while loop and single value check
        while (b & MASK) > 0: 
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # Handles negatives if the last carry left is greater than the max 32-bit positive integer
        return (a & MASK) if (b > MASK) else a