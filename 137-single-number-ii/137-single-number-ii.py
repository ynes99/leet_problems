class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(list(set(nums))*3)-sum(nums))//2
    #use sums and maths and shit 