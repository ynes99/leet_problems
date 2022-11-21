class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(set(numbers)) == len(numbers):
        # brute force Broooo
            
            for i in range(len(numbers)-1):
                for j in range(i+1, len(numbers)):
                    sum_tmp = numbers[i]+numbers[j]
                    if sum_tmp == target:
                        return[i+1,j+1]
        
        else:
            l,r = 0 , len(numbers)-1
            while l!=r:
                print(r,l)
                curr_sum = numbers[l]+numbers[r]
                if curr_sum > target : r -= 1
                elif curr_sum < target : l += 1
                else: return([l+1,r+1])
