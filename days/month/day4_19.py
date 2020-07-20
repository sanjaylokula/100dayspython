import numpy as np

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)
        j = len(b)
        if i > j:
            A_a = np.array(list(a), dtype=int)
            B_a = np.array([0 for k in range(i - j)] + list(b), dtype=int)
        else:
            B_a = np.array(list(b), dtype=int)
            A_a = np.array([0 for k in range(abs(i - j))] + list(a), dtype=int)
        sum_AB = A_a + B_a
        length = len(sum_AB)
        carry = 0
        for each in range(length):

            if carry == 0:
                if sum_AB[length - each - 1] == 2:
                    carry = 1
                    sum_AB[length - each - 1] = 0
            else:
                if sum_AB[length - each - 1] == 2:
                    carry = 1
                    sum_AB[length - each - 1] = 1
                elif sum_AB[length - each - 1] == 1:
                    carry = 1
                    sum_AB[length - each - 1] = 0
                else:
                    sum_AB[length - each - 1] = 1
                    carry = 0
        if carry > 0:
            sum_AB = np.append([1], sum_AB)
        return ''.join(map(str, sum_AB.tolist()))


if __name__=="__main__":
    output=Solution().addBinary('11','1')
    print(output)