class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        for i in range(len(nums)):
            while (nums.count(nums[i]) > 2):
                nums.pop(i)
                if nums.count(nums[i]) <= 2:
                    break
        """
        s = set(nums)
        d = dict()
        for v in s :
            d[v] = nums.count(v)
        c=0
        print(d)
        for key,value in d.items():
            print(key,value)
            if value == 1 :
                nums[c] = key
                c+=1
            else:
                for i in range(2):
                    nums[c] = key
                    c+=1
        for i in range(len(nums)-c):
            nums.pop()
        nums.sort()    