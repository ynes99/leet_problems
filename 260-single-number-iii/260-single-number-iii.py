class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        setNum = set()
        for num in nums:
            if num in setNum:
                setNum.remove(num)
            else:
                setNum.add(num)
        return setNum