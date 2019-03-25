# py3 one-pass hash
# 关键点,利用字典的key是hash过的这点来减少循环嵌套,减少时间复杂度.

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
