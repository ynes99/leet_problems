class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        if len(colors) < 3:
            return(False)
        count_B = 0
        count_A = 0
        for i in range(1,len(colors)-1):
            # checking if both its neighbors are also colored the same 
            if colors[i] == colors[i+1] == colors[i-1] : 
                if colors[i] == 'A':
                    count_A +=1
                else:
                    count_B +=1
        #print('Bob played :',count_B,' times and Alice played:',count_A,' times')
        if count_A <= count_B:
            return(False)
        else:
            return(True)