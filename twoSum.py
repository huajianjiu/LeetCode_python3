# py3 one-pass hash

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_number = {}
        for i, v in enumerate(nums):
            try:
                j = index_number[target-v]
                if i>j:
                    return [j,i]
                else:
                    return [i,j]
            except KeyError:
                index_number[v]=i
                continue
