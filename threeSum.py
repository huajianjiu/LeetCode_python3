#重点: 1.in set比in list快; 2.分为000, 负0正, 负负正, 正正负以缩小搜索空间.
#特别注意分为负负正和正正负比找正负然后讨论第三个数来得快 -- 因为第二个数只需要寻找第一个数的右边即可. 并且可以简单解决重复数字的问题.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set([])
        positive_nums = []
        negative_nums = []
        zeros = []
        for v in sorted(nums):
            if v<0:
                negative_nums.append(v)
            elif v==0:
                zeros.append(v)
            else:
                positive_nums.append(v)
        negative_nums = sorted(negative_nums)
        positive_nums = sorted(positive_nums)
        negative_nums_hash = set(negative_nums)
        positive_nums_hash = set(positive_nums)
        if len(zeros)>2:
            results.add((0,0,0))
        if len(zeros)>0:
            for x in negative_nums_hash:
                if -x in positive_nums_hash:
                    results.add((x,0,-x))
                else:
                    continue
        if len(negative_nums)>1:
            for i, x in enumerate(negative_nums):
                for y in negative_nums[i+1:]:
                    z = -(x+y)
                    if z in positive_nums_hash:
                        results.add((x,y,z))
                    else:
                        continue
        if len(positive_nums)>1:
            for i, y in enumerate(positive_nums):
                for z in positive_nums[i+1:]:
                    x = -(y+z)
                    if x in negative_nums_hash:
                        results.add((x,y,z))
                    else:
                        continue
        return list(results)
