class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def dfs(i,j,ind):
            if(ind==len(word)):
                return True
            if(i<0 or i>=n or j<0 or j>=m or board[i][j]!=word[ind]):
                return False
            temp=board[i][j]
            board[i][j]="#"
            #four directions are top,down,left and right
            found=(dfs(i-1,j,ind+1) or dfs(i+1,j,ind+1) or 
            dfs(i,j-1,ind+1) or dfs(i,j+1,ind+1))
            board[i][j]=temp
            return found 
        #now again iterate and if dfs is True return True else False
        for i in range(0,n):
            for j in range(0,m):
                if(dfs(i,j,0)):
                    return True
        return False


       