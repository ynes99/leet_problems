class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        right_pointer = len(nums)-1
        left_pointer = 0
        res = []
        
        while left_pointer <= right_pointer:
            
            if abs(nums[left_pointer]) >= abs(nums[right_pointer]):
                
                res.append(nums[left_pointer]**2)
                left_pointer += 1
                
            else:
                
                res.append(nums[right_pointer]**2)
                right_pointer -= 1
                
        
        return(res[::-1])