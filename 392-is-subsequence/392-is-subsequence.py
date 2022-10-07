class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s)==0:
            return True
        subsequence = 0
        for index_t in range(len(t)):
            if subsequence <= len(s) -1:
                if t[index_t] == s[subsequence]:
                    subsequence +=1
        if subsequence == len(s):
                return True
            