from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums1=nums.copy()
        for i,j in enumerate(nums):
            diff=target-j
            if diff in nums and nums.index(diff)!=i:
                return [i,nums.index(diff)]

if __name__=="__main__":
    output=Solution().twoSum([2,7,11,15],9)
    print(output)