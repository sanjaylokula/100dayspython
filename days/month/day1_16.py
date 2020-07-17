class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = -1 * n if n < 0 else n
        flag = 1 if power % 2 == 0 else x
        if power % 2 == 0:
            return ((x ** (n / 2)) ** 2) * flag
        else:
            return ((x ** ((n - 1) / 2)) ** 2) * flag

if __name__ =="__main__":
    output=Solution().myPow(2,4)
    print(output)
