
#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#Example 2:

#Input: -123
#Output: -321
#Example 3:

#Input: 120
#Output: 21
#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:

        length = len(str(abs(x)))
        reverse = 0
        y = x
        for i in range(length):
            reverse = reverse + ((abs(y) % 10) * (10 ** (length - i - 1)))
            y = abs(y) // 10
        if x < 0:
            reverse = -1 * reverse
        else:
            reverse = reverse
        if (2 ** 31) - 1 <= reverse or reverse <= (-2) ** 31:
            return 0
        else:
            return reverse

if __name__=="__main__":
    output=Solution().reverse(1534236469)
    print(output)