#Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

#Example:

#Input:  [1,2,1,3,2,5]
#Output: [3,5]
#Note:

#The order of the result is not important. So in the above example, [5, 3] is also correct.
#Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output_dict = dict()
        for i in nums:
            if i not in output_dict:
                output_dict[i] = 1
            else:
                output_dict[i] += 1

        return [key for key, value in output_dict.items() if value == 1]

if __name__=="__main__":
    output=Solution().singleNumber([1,2,3,4,2,1,2])
    print(output)