class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #first perform the swap and then reverse the rows
        n=len(matrix)
        for i in range(0,n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #now again traverse through rows and reverse
        for i in range(0,n):
            matrix[i]=matrix[i][::-1]
        return matrix
            

       