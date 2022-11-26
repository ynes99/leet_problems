class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positives=[] 
        negatives=[]
        zeros=0
        output=set()
        nums.sort()
        for num in nums:
            if num>0:
                positives.append(num)
            elif num<0:
                negatives.append(num)    
            else: 
                zeros=zeros+1

        P, N = set(positives), set(negatives) 

        PosTotal=len(positives)
        negTotal= len(negatives)

        for a in range(PosTotal):
            for b in range(a+1,PosTotal):
                Target=(positives[a]+positives[b])*(-1)
                if Target in N:
                    output.add(tuple((positives[a],positives[b],Target)))
        for a in range(negTotal):
            for b in range(a+1,negTotal):
                target=(negatives[a]+negatives[b])*-1
                if target in P:
                    output.add(tuple((target,negatives[a],negatives[b])))
        if zeros!=0:
            for p in positives:
                if -p in N:
                    output.add((p,-p,0))
        if zeros>2:
            output.add((0,0,0))
        
        return output
