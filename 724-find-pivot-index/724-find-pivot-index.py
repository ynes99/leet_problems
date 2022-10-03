class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=0
        right_sum = sum(nums)
        for i in range(len(nums)) :
            left_sum = s
            print(s)
            right_sum -=nums[i]
            print(right_sum)
            if right_sum == left_sum :
                return(i)
            s+=nums[i]
        return(-1)    
        