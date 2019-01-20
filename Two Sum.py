class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {} # key is num, value is index
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], i]
            dic[num] = i
