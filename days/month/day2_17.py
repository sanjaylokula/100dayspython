from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = dict()
        output_list = []
        for i in nums:
            if i in output:
                output[i] += 1
            else:
                output[i] = 1
        t = sorted(output.items(), key=lambda x: x[1], reverse=True)[:k]
        for key, value in t:
            output_list.append(key)

        return output_list

if __name__ == "__main__":
    output=Solution().topKFrequent([1,1,1,2,2,3],2)
    print(output)