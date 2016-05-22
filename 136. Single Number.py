class Solution(object):
    def singleNumber(self, nums):
        result=0
        if len(nums)==0:
            return 0
        for i in nums:
            result^=i
        return result
