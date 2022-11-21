class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # order whatever
        end = -1
        i = 0
        while i != (end + len(nums) +1):
            print(end + len(nums))
            print(nums)
            if nums[i] == 0 :
                nums[i],nums[end] = nums[end],nums[i]
                end -= 1
            i += 1
        """
        firstZero = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[firstZero], nums[i] = nums[i], nums[firstZero]
                firstZero += 1


