class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #lets do it for rows,cols and subboxes
        n=len(board)
        m=len(board)
        for r in range(0,9):
            rowset=set()
            for c in range(0,9):
                if(board[r][c]=="."):
                    continue
                if(board[r][c] in rowset):
                    return False
                rowset.add(board[r][c])
        #now similarly do for cols 
        for c in range(0,9):
            colset=set()
            for r in range(0,9):
                if(board[r][c]=="."):
                    continue
                if(board[r][c] in colset):
                    return False
                colset.add(board[r][c])
        #now at last do for subboxes which are of size 3*3
        for sr in range(0,9,3):
            er=sr+2
            for sc in range(0,9,3):
                ec=sc+2
                #now the next step is to check for validity
                if(not self.isValid(sr,er,sc,ec,board)):
                    return False
        return True 
    
    def isValid(self,sr,er,sc,ec,board):
        n=len(board)
        m=len(board[0])
        st=set()
        for i in range(sr,er+1):
            for j in range(sc,ec+1):
                if(board[i][j]=="."):
                    continue
                if(board[i][j] in st):
                    return False
                st.add(board[i][j])
        return True







        