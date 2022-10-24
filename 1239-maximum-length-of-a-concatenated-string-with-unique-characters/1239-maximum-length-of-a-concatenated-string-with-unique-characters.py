class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]

        for seq in arr:
            chars = set(seq)

            if len(chars) < len(seq):
                continue

            dp.extend(chars | other for other in dp if not (chars & other))

        return max(map(len, dp))
        
        
        
        
        
        
        
        """        
        n_arr =[]
        
        for string in arr :
            if len(set(string)) == len(string):
                n_arr.append(s)
                
        if len(arr) == 0 :
            return(0)
        
        if len(arr) == 1 :
            return(len(arr[0]))


        s_arr = sorted(n_arr, key=len)
        ch = s_arr[-1]+ s_arr[-2]
        
        while 
        if len(set(ch) == len(ch):
            length = len(s_arr[-1])+len(s_arr[-2])
        """

        