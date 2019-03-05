class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dic:
                return [dic[diff], index]
            else:
                dic[value] = index
